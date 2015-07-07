from __future__ import absolute_import, print_function

'''findit/findit.py

    Provides FindIt object, providing a tidy object layer
        into the logic.get_pdf_from_pma function. (see logic.py)

    The FindIt class allows lookups of the PDF starting from only a
    DOI or a PMID, using the following instantiation approaches:

    source = FindIt('1234567')   # assumes argument is a pubmed ID

    source = FindIt(pmid=1234567)  # pmid can be an int or a string

    source = FindIt(doi="10.xxxx/xxx.xxx")   # doi instead of pmid.

    See the FindIt docstring for more information.

    *** IMPORTANT NOTE ***

    In many cases, this code performs intermediary HTTP requests in order to
    scrape a PDF url out of a page, and sometimes tests the url to make sure
    that what's being sent back is in fact a PDF.

    If you would like these requests to go through a proxy (e.g. if you would
    like to prevent making multiple requests of the same servers, which may have
    effects like getting your IP shut off from PubMedCentral), set the
    HTTP_PROXY environment variable in your code or on the command line before
    using any FindIt functionality.
'''

__author__ = 'nthmost'

from urlparse import urlparse

import requests
import os, time
import logging

from ..exceptions import MetaPubError
from ..pubmedfetcher import PubMedFetcher
from ..convert import PubMedArticle2doi_with_score, doi2pmid
from ..eutils_common import SQLiteCache, get_cache_path

from .logic import find_article_from_pma
from .dances import the_sciencedirect_disco, the_doi_2step, the_wiley_shuffle
from .cache_utils import datetime_to_timestamp

FETCH = PubMedFetcher()

DEFAULT_CACHE_DIR = os.path.join(os.path.expanduser('~'), '.cache')
CACHE_FILENAME = 'findit-cache.db'

FINDIT_CACHE = None

def _get_findit_cache(cachedir=DEFAULT_CACHE_DIR):
    global FINDIT_CACHE
    if not FINDIT_CACHE:
        _cache_path = get_cache_path(cachedir, CACHE_FILENAME)
        FINDIT_CACHE = SQLiteCache(_cache_path)
    return FINDIT_CACHE

class FindIt(object):
    ''' FindIt

        FindIt helps locate an article's fulltext PDF based on its pubmed ID
        or doi, using the following instantiation approaches:

        source = FindIt('1234567')   # assumes argument is a pubmed ID

        source = FindIt(pmid=1234567)  # pmid can be an int or a string

        source = FindIt(doi="10.xxxx/xxx.xxx")   # doi instead of pmid.

        The machinery in the FindIt object performs all necessary data lookups
        (e.g. looking up a missing DOI, or using a DOI to get a PubMedArticle)
        to end up with a url and reason, which attaches to the FindIt object
        in the following attributes:

        source = FindIt(pmid=PMID)
        source.url
        source.reason
        source.pmid
        source.doi
        source.doi_score

        The "doi_score" is an indication of where the DOI for this PMID ended up
        coming from. If it was supplied by the user or by PubMed, doi_score will be 10.
        If CrossRef came into play during the process to find a DOI that was missing
        for the PubMedArticle object, the doi_score will come from the CrossRef "top
        result".
    '''

    def __init__(self, pmid=None, **kwargs):
        self.pmid = pmid if pmid else kwargs.get('pmid', None)
        self.doi = kwargs.get('doi', None)
        self.url = kwargs.get('url', None)
        self.reason = None
        self.use_nih = kwargs.get('use_nih', False)
        self.use_crossref = kwargs.get('use_crossref', True)
        self.doi_min_score = kwargs.get('doi_min_score', 2.3)
        self.tmpdir = kwargs.get('tmpdir', '/tmp')
        self.doi_score = None
        self.pma = None
        self._backup_url = None

        retry_errors = kwargs.get('retry_errors', False)

        cachedir = kwargs.get('cachedir', DEFAULT_CACHE_DIR)
        self._cache = None if cachedir is None else _get_findit_cache(cachedir)

        self._log = logging.getLogger('metapub.FindIt')
        if kwargs.get('debug', False):
            self._log.setLevel(logging.DEBUG)
        else:
            self._log.setLevel(logging.INFO)

        if self.pmid:
            self._load_pma_from_pmid()
        elif self.doi:
            self._load_pma_from_doi()
        else:
            raise MetaPubError(
                'Supply either a pmid or a doi to instantiate. e.g. FindIt(pmid=1234567)')

        try:
            if self._cache:
                self.url, self.reason = self.load_from_cache(retry_errors)
            else:
                self.url, self.reason = self.load()
        except requests.exceptions.ConnectionError as error:
            self.url = None
            self.reason = 'TXERROR: %r' % error

    def load(self):
        '''interface to logic.find_article_from_pma; uses self.pma to return
        a (url, reason) tuple.

        If url is None, reason should have a string.  If url is not None, there may
        or may not be a reason string (usually not).

        If a ConnectionError prevented lookup, returns (None, "TXERROR: <info>")

        :return: (url, reason) (string or None, string or None)
        '''
        return find_article_from_pma(self.pma, use_nih=self.use_nih)

    def load_from_cache(self, retry_errors=False):
        '''Using preloaded identifiers (self.pmid, self.doi, etc), check cache
        for article lookup results. If it's not in the cache, call self.load()
        and store the results in the cache.

        If url is None, reason should have a string.  If url is not None, there may
        or may not be a reason string (usually not).

        If self.load() comes up as a ConnectionError (usually indicating a problem
        with the internet connection), no result will be cached.

        If cache result has reason like "NOFORMAT", "TODO", "PAYWALL", or "CANTDO",
        try a fresh load; there are new formats added to FindIt all the time. :)

        :return: (url, reason) (string or None, string or None)
        '''
        retry_reasons = ['PAYWALL', 'TODO', 'NOFORMAT', 'CANTDO']
        if retry_errors:
            retry_reasons.append('TXERROR')

        cache_result = self._query_cache(self.pmid)
        if cache_result:
            url = cache_result['url']
            reason = '' if cache_result['reason'] is None else cache_result['reason']
            if not reason.split(':')[0] in retry_reasons:
                return (url, reason)

        url, reason = self.load()
        self._store_cache(self.pmid, url=url, reason=reason)
        return (url, reason)

    @property
    def backup_url(self):
        '''Returns a backup url to try if the first url doesn't pan out.'''
        if not self.doi:
            return None

        if self._backup_url is not None:
            return self._backup_url

        try:
            baseurl = the_doi_2step(self.doi)
        except MetaPubError as error:
            self._log.debug('%r', error)
            return None

        urlp = urlparse(baseurl)

        # maybe it's sciencedirect / elsevier:
        if urlp.hostname.find('sciencedirect') > -1 or urlp.hostname.find('elsevier') > -1:
            if self.pma.pii:
                try:
                    self._backup_url = the_sciencedirect_disco(self.pma)
                except Exception as error:
                    self._log.debug('%r', error)

        # maybe it's wiley:
        elif urlp.hostname.find('wiley') > -1:
            try:
                self._backup_url = the_wiley_shuffle(self.pma)
            except Exception as error:
                self._log.debug('%r', error)

        #TODO maybe it's an "early" print? if so it might look like this:
        #
        # if urlp.path.find('early'):
        #    return None

        if self._backup_url is None and urlp.path.find('.') > -1:
            extension = urlp.path.split('.')[-1]
            if extension == 'long':
                self._backup_url = baseurl.replace('long', 'full.pdf')
            elif extension == 'html':
                self._backup_url = baseurl.replace(
                    'full', 'pdf').replace('html', 'pdf')

        if self._backup_url is None:
            # a shot in the dark...
            if urlp.path.endswith('/'):
                self._backup_url = baseurl + 'pdf'
            else:
                self._backup_url = baseurl + '.full.pdf'

        return self._backup_url

    def _load_pma_from_pmid(self):
        '''loads self.pma if self.pmid is present.

        Mutates:
            self.doi (using crossref to look this information up if necessary)
            self.doi_score (10.0 if doi found in self.pma, else crossref score)
        '''

        self.pma = FETCH.article_by_pmid(self.pmid)
        if self.pma.doi:
            self.doi = self.pma.doi
            self.doi_score = 10.0

        if self.pma.doi == None:
            if self.use_crossref:
                self.pma.doi, self.doi_score = PubMedArticle2doi_with_score(
                    self.pma, min_score=self.doi_min_score)
                if self.pma.doi == None:
                    self.reason = 'MISSING: doi (CrossRef lookup failed)'
                else:
                    self.doi = self.pma.doi

    def _load_pma_from_doi(self):
        '''loads self.pma if self.doi is present.

        Mutates:
            self.pmid (using metapub.convert.doi2pmid)
            self.pma  (if pmid was found)
            self.doi_score (10.0 if doi found in self.pma, else crossref score)
        '''
        self.pmid = doi2pmid(self.doi)
        if self.pmid:
            self.pma = FETCH.article_by_pmid(self.pmid)
            self.doi_score = 10.0
        else:
            raise MetaPubError('Could not get a pmid for doi %s' % self.doi)

    def to_dict(self):
        '''returns a dictionary containing the public attributes of this object'''
        return {'pmid': self.pmid,
                'doi': self.doi,
                'reason': self.reason,
                'url': self.url,
                'doi_score': self.doi_score,
               }

    def _store_cache(self, cache_key, **kwargs):
        '''Store supplied cache_key pointing to values supplied in kwargs.

        A time.time() timestamp will be added to the value dictionary when stored.

        There is no return from this function. Exceptions from the SQLiteCache 
        object may be raised.
        '''
        cache_value = kwargs.copy()
        cache_value['timestamp'] = time.time()
        self._cache[cache_key] = cache_value

    def _query_cache(self, pmid, expiry_date=None):
        '''Return results of a lookup from the cache, if available.
        Return None if not available.

        Cache results are stored with a time.time() timestamp.

        When expiry_date is supplied, results from the cache past their
        sell-by date will be expunged from the cache and return will be None.

        expiry_date can be either a python datetime or a timestamp. 

        :param: cache_key: (required)
        :param: expiry_date (optional, default None)
        :rtype: (url, reason) or None
        '''

        if hasattr(expiry_date, 'strftime'):
            # convert to timestamp
            sellby = datetime_to_timestamp(expiry_date)
        else:
            sellby = expiry_date

        if self._cache:
            cache_key = pmid
            try:
                res = self._cache[cache_key]
                timestamp = res['timestamp']
                if timestamp < sellby:
                    self._log.debug('Cache: expunging result for %s (%i)', cache_key, timestamp)
                else:
                    self._log.debug('Cache: returning result for %s (%i)', cache_key, timestamp)
                return res

            except KeyError:
                self._log.debug('Cache: no result for key %s', cache_key)
                return None
        else:
            self._log.debug('Cache disabled (self._cache is None)')
            return None

