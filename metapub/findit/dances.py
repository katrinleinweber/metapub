from __future__ import absolute_import, print_function

__author__='nthmost'

import requests
from lxml.html import HTMLParser
from lxml import etree

from ..exceptions import MetaPubError, AccessDenied, NoPDFLink
from ..text_mining import re_numbers
from ..utils import asciify

from .journal_formats import *


DX_DOI_URL = 'http://dx.doi.org/%s'
def the_doi_2step(doi):
    'takes a DOI (string), returns a url to a paper'
    response = requests.get(DX_DOI_URL % doi)
    if response.status_code in [200, 401, 301, 302, 307, 308]:
        return response.url
    else:
        raise NoPDFLink('dx.doi.org lookup failed for doi %s (HTTP %i returned)' % (doi, response.status_code))

def square_voliss_data_for_pma(pma):
    '''takes a PubMedArticle object, returns same object with corrected volume/issue 
    information (if needed)'''
    if pma.volume != None and pma.issue is None:
        # try to get a number out of the parts that came after the first number.
        volparts = re_numbers.findall(pma.volume)
        if len(volparts) > 1:
            pma.volume = volparts[0]
            # take a guess. best we can do. this often works (e.g. Brain journal)
            pma.issue = volparts[1]
    if pma.issue and pma.volume:
        if pma.issue.find('Pt') > -1:
            pma.issue = re_numbers.findall(pma.issue)[0]
    return pma

sciencedirect_url = 'http://www.sciencedirect.com/science/article/pii/{piit}'
def the_sciencedirect_disco(pma):
    '''  :param: pma (PubMedArticle object)
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    #we're looking for a url that looks like this:
    #http://www.sciencedirect.com/science/article/pii/S0022283601953379/pdfft?md5=07db9e1b612f64ea74872842e34316a5&pid=1-s2.0-S0022283601953379-main.pdf

    starturl = None
    if pma.pii:
        starturl = sciencedirect_url.format(piit = pma.pii.translate(None,'-()'))
    elif pma.doi:
        starturl = the_doi_2step(pma.doi)

    if starturl == None:
        raise NoPDFLink('pii missing from PubMedArticle XML (needed for ScienceDirect link) AND doi lookup failed. Harsh!') 

    try:
        r = requests.get(starturl)
    except requests.exceptions.TooManyRedirects:
        raise NoPDFLink('TooManyRedirects: cannot reach %s via %s' % (pma.journal, starturl))

    tree = etree.fromstring(r.text, HTMLParser())
    div = tree.cssselect('div.icon_pdf')[0]
    url = div.cssselect('a')[0].get('href')
    if url.find('.pdf') > -1:
        return url
    else:
        # give up, it's probably a "shopping cart" link.
        # TODO: parse return, raise more nuanced exceptions here.
        raise NoPDFLink('cannot find pdf link (probably behind paywall)')

def the_biomed_calypso(pma):
    baseid = pma.doi if pma.doi else pma.pii
    if baseid:
        article_id = baseid.split('/')[1]
    else:
        raise NoPDFLink('BMC article requires DOI (none extant)')
    return BMC_format.format(aid=article_id)


def the_aaas_tango(pma):
    ja = aaas_journals[pma.journal]
    if pma.volume and pma.issue and pma.first_page:
        url = aaas_format.format(ja=ja, a=pma)
    elif pma.doi:
        url = the_doi2step(pma.doi)
    else:
        raise NoPDFLink('Not enough information in PubMedArticle for AAAS journal.')
    return url


def the_jama_dance(pma):
    '''  :param: pma (PubMedArticle object)
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    url = the_doi_2step(pma.doi)
    r = requests.get(url)
    parser = HTMLParser()
    tree = etree.fromstring(r.text, parser)
    # we're looking for a meta tag like this:
    # <meta name="citation_pdf_url" content="http://archneur.jamanetwork.com/data/Journals/NEUR/13776/NOC40008.pdf" />
    for item in tree.findall('head/meta'):
        if item.get('name')=='citation_pdf_url':
            return item.get('content')
    raise NoPDFLink('could not find PDF url in JAMA page (%s).' % url)

def the_jstage_dive(pma):
    '''  :param: pma (PubMedArticle object)
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    url = the_doi_2step(pma.doi)
    r = requests.get(url)
    if r.url.find('jstage') > -1:
        return r.url.replace('_article', '_pdf')
    else:
        raise NoPDFLink('%s did not resolve to jstage article' % url)

def the_wiley_shuffle(pma):
    '''  :param: pma (PubMedArticle object)
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    r = requests.get(format_templates['wiley'].format(a=pma))
    if r.headers['content-type'].find('html') > -1:
        if r.text.find('ACCESS DENIED') > -1:
            raise AccessDenied('Wiley says ACCESS DENIED to %s' % r.url)

        tree = etree.fromstring(r.text, HTMLParser())
        if tree.find('head/title').text.find('Not Found') > -1:
            raise NoPDFLink('Wiley says File Not found (%s)' % r.url)
        iframe = tree.find('body/div/iframe')
        return iframe.get('src')

    elif r.headers['content-type'] == 'application/pdf':
        return r.url

def the_lancet_tango(pma):
    '''  :param: pma (PubMedArticle object)
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    if pma.pii:
        return format_templates['lancet'].format(a = pma, ja=lancet_journals[pma.journal.translate(None, '.')]['ja'])
    if pma.doi:
        return the_doi_2step(pma.doi).replace('abstract', 'pdf').replace('article', 'pdfs')
    else:
        raise NoPDFLink('pii missing from PubMedArticle XML and DOI lookup failed. Harsh!')

def the_nature_ballet(pma):
    '''  :param: pma (PubMedArticle object)
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    url = ''
    if pma.doi:
        try:
            starturl = the_doi_2step(pma.doi)
            url = starturl.replace('html', 'pdf').replace('abs', 'pdf').replace('full', 'pdf')
        except NoPDFLink:
            # alright, let's try the pii route.
            pass

    if url=='':
        if pma.pii:
            print('URL: ', url)
            url = nature_format.format(a=pma, ja=nature_journals[pma.journal.translate(None, '.')]['ja'])
        else:
            if pma.doi:
                print('DOI: ', pma.doi)
                raise NoPDFLink('the_doi2step failed and no PII in metadata')
            else:
                print('pii: ', pma.pii)
                raise NoPDFLink('not enough information to compose a link for Nature (no DOI or PII)')

    r = requests.get(url)
    if r.headers['content-type'].find('pdf') > -1:
        return r.url
    elif r.headers['content-type'].find('html') > -1:
        raise AccessDenied('Nature denied access to %s' % r.url)
    raise NoPDFLink('unknown problem retrieving from %s' % r.url)

paywall_reason_template = '%s behind %s paywall'  # % (journal, publisher)


PMC_PDF_URL = 'http://www.ncbi.nlm.nih.gov/pmc/articles/pmid/{a.pmid}/pdf'
EUROPEPMC_PDF_URL = 'http://europepmc.org/backend/ptpmcrender.fcgi?accid=PMC{a.pmc}&blobtype=pdf'
def the_pmc_twist(pma):
    '''  :param: pma (PubMedArticle object)
         :return: url
         :raises: NoPDFLink
    '''
    url = EUROPEPMC_PDF_URL.format(a=pma)
    # TODO: differentiate between paper embargo and URL block.
    #       URL block might be discerned by grepping for this:
    #
    #   <div class="el-exception-reason">Bulk downloading of content by IP address [162.217...,</div>
    r = requests.get(url)
    if r.headers['content-type'].find('html') > -1:
        url = PMC_PDF_URL.format(a=pma)
        # try the other PMC.
        r = requests.get(url)
        if r.headers['content-type'].find('html') > -1:
            raise NoPDFLink('could not get PDF url from either NIH or EuropePMC.org')

    if r.headers['content-type'].find('pdf') > -1:
        return url

    raise NoPDFLink('PMC download returned weird content-type %s' % r.headers['content-type'])


def find_article_from_pma(pma, use_crossref=True, use_paywalls=False):
    ''' The real workhorse of FindIt.

        Based on the contents of the supplied PubMedArticle object, this function
        returns the best possible download link for a Pubmed PDF.

        Returns (url, reason) -- url being self-explanatory, and "reason" containing
        any qualifying message about why the url came back the way it did.

        Reasons may include (but are not limited to):

            "DOI missing from PubMedArticle and CrossRef lookup failed."
            "pii missing from PubMedArticle XML"
            "No URL format for Journal %s"
            "TODO format"

        :param: (pma PubMedArticle object) 
        :param: use_crossref (bool) default: True
        :param: use_paywalls (bool) default: False [not yet implemented]
        :return: (url, reason)
    '''
    reason = None
    url = None

    # protect against unicode character mishaps in journal names.
    # (did you know that unicode.translate takes ONE argument whilst str.translate takes TWO?! true story)
    jrnl = asciify(pma.journal).translate(None, '.')

    if pma.pmc:
        try:
            url = the_pmc_twist(pma)
            return (url, None)
        except Exception, e:
            reason = str(e)

    if pma.doi==None and use_crossref:
        pma.doi = PubMedArticle2doi(pma)
        if pma.doi==None:
            reason = 'DOI missing from PubMedArticle and CrossRef lookup failed.'
        else:
            reason = 'DOI missing from PubMedArticle.'
 
    if jrnl in simple_formats_pii.keys():
        # TODO: find a smarter way to process these (maybe just break them out into publishers)
        if pma.pii:
            url = simple_formats_pii[jrnl].format(a=pma)
            reason = ''
        elif pma.doi:
            try:
                url = the_doi_2step(pma.doi)
            except MetaPubError, e:
                reason = '%s' % e
        else:
            url = None
            reason = 'pii missing from PubMedArticle XML and DOI lookup failed. Harsh!'

        if url:
            r = requests.get(url)
            if r.text.find('Access Denial') > -1:
                url = None
                reason = 'Access Denied by ScienceDirect'

    elif jrnl in simple_formats_doi.keys():
        if pma.doi:
            url = simple_formats_doi[jrnl].format(a=pma)
            reason = ''

    #elif jrnl in doi2step_journals:
    #    if pma.doi:
    #        try:
    #            baseurl = the_doi_2step(pma.doi)
    #            url = baseurl.replace('full', 'pdf').replace('html', 'pdf')
    #            reason = ''
    #        except Exception, e:
    #            reason = '%s' % e

    elif jrnl in jstage_journals:
        if pma.doi:
            try:
                url = the_jstage_dive(pma)
            except Exception, e:
                reason = str(e)

    elif jrnl.find('BMC')==0 or jrnl in BMC_journals:
        # Many Biomed Central journals start with "BMC", but many more don't.
        try:
            url = the_biomed_calypso(pma)
        except Exception, e:
            reason = str(e)
            
    elif jrnl in wiley_journals:
        if pma.doi:
            try:
                url = the_wiley_shuffle(pma)
            except Exception, e:
                reason = str(e)

    elif jrnl in jama_journals:
        try:
            url = the_jama_dance(pma)
        except Exception, e:
            reason = str(e)

    elif jrnl in vip_journals.keys(): 
        pma = square_voliss_data_for_pma(pma)
        if pma.volume and pma.issue:
            url = vip_format.format(host=vip_journals[jrnl]['host'], a=pma)
        else:
            # TODO: try the_doi_2step
            reason = 'volume and maybe also issue data missing from PubMedArticle'

    elif jrnl in spandidos_journals.keys():
        pma = square_voliss_data_for_pma(pma)
        if pma.volume and pma.issue:
            url = spandidos_format.format(ja=spandidos_journals[jrnl]['ja'], a=pma)
        else:
            # TODO: try the_doi_2step
            reason = 'volume and maybe also issue data missing from PubMedArticle'

    elif jrnl in nature_journals.keys():
        try:
            url = the_nature_ballet(pma)
        except Exception, e:
            reason = str(e)

    elif jrnl in cell_journals.keys():
        if pma.pii:
            # the front door
            url = cell_format.format( a=pma, ja=cell_journals[jrnl]['ja'],
                    pii=pma.pii.translate(None,'-()') )
        #elif pma.doi:
            # the side door
        #    try:
        #        baseurl = the_doi_2step(pma.doi)
        #        url = baseurl.replace('full', 'pdf').replace('html', 'pdf')
        #        reason = ''
        #    except Exception, e:
        #        reason = '%s' % e
        else:
            #reason = 'pii missing from PubMedArticle XML (%s in Cell format) and no DOI either (harsh!)' % jrnl
            reason = 'pii missing from PubMedArticle XML (%s in Cell format)' % jrnl

    elif jrnl.find('Lancet') > -1:
        try:
            url = the_lancet_tango(pma)
        except Exception, e:
            reason = str(e)

    elif jrnl in sciencedirect_journals:
        try:
            url = the_sciencedirect_disco(pma)
        except Exception, e:
            reason = str(e)

    elif jrnl in paywall_journals:
        if use_paywalls:
            reason = '%s behind paywall; not yet smart enough to navigate paywalls, sorry!' % jrnl
        else:
            reason = '%s behind paywall' % jrnl

    elif jrnl in todo_journals:
        reason = 'TODO format -- example: %s' % todo_journals[jrnl]['example']

    elif jrnl in FINDIT_CANTDO_LIST:
        reason = 'this journal is in the "can\'t do" list'

    else:
        reason = 'No URL format for Journal %s' % jrnl

    return (url, reason)


def find_article_from_doi(doi):
    '''pull a PubMedArticle based on CrossRef lookup (using doi2pmid),
    then run it through find_article_from_pma.

        :param: doi (string)
        :return: (url, reason)
    '''
    pma = fetch.article_by_pmid(doi2pmid(doi))
    return find_article_from_pma(pma)
    


class FindIt(object):

    @classmethod
    def by_pmid(cls, pmid, *args, **kwargs):
        kwargs['pmid'] = pmid
        return cls(args, kwargs)

    @classmethod
    def by_doi(cls, doi, *args, **kwargs):
        kwargs['doi'] = doi
        return cls(args, kwargs)
    
    def __init__(self, *args, **kwargs):    
        self.pmid = kwargs.get('pmid', None)
        self.doi = kwargs.get('doi', None)
        self.url = kwargs.get('url', None)
        self.reason = None
        self.use_crossref = kwargs.get('use_crossref', True)
        self.use_paywalls = kwargs.get('use_paywalls', False)
        self.doi_min_score = kwargs.get('doi_min_score', 2.3)
        self.tmpdir = kwargs.get('tmpdir', '/tmp')
        self.doi_score = None
        self.pma = None

        if self.pmid:
            self._load_pma_from_pmid()
        elif self.doi:
            self._load_pma_from_doi()

        try:
            self.url, self.reason = find_article_from_pma(self.pma, use_paywalls=self.use_paywalls) 
        except requests.exceptions.ConnectionError, e:
            self.url = None
            self.reason = 'tx_error: %r' % e


    def _load_pma_from_pmid(self):
        self.pma = fetch.article_by_pmid(self.pmid)
        if self.pma.doi:
            self.doi_score==10.0
        
	if self.pma.doi==None:
            if self.use_crossref:
	        self.pma.doi, self.doi_score = PubMedArticle2doi_with_score(self.pma, min_score=self.doi_min_score)
                if self.pma.doi == None:
                    self.reason = 'DOI missing from PubMedArticle and CrossRef lookup failed.'

    def _load_pma_from_doi(self):
        self.pmid = doi2pmid(doi)
        self.pma = fetch.article_by_pmid(self.pmid)
        self.doi_score = 10.0

    def to_dict(self):
        return { 'pmid': self.pmid,
                 'doi': self.doi,
                 'reason': self.reason,
                 'url': self.url,
                 'doi_score': self.doi_score,
               }
