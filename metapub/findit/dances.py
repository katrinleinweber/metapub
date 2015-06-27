from __future__ import absolute_import, print_function

__author__='nthmost'

from urlparse import urljoin, urlsplit

import requests
from lxml.html import HTMLParser
from lxml import etree

from ..exceptions import MetaPubError, AccessDenied, NoPDFLink
from ..text_mining import re_numbers
from ..utils import asciify

from .journal_formats import *

#TODO: make configurable (somehow...)
AAAS_USERNAME = 'nthmost'
AAAS_PASSWORD = '434264'


DX_DOI_URL = 'http://dx.doi.org/%s'
def the_doi_2step(doi):
    'takes a doi (string), returns a url to a paper'
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

def the_jci_polka(pma):
    '''Dance of the Journal of Clinical Investigation, which should be largely free.

         :param: pma (PubMedArticle object)
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    # approach: pii with dx.doi.org fallback to get pdf "view" page; scrape pdf download link.
    if pma.pii:
        starturl = format_templates['jci'].format(a=pma)
    elif pma.doi:
        starturl = the_doi_2step(pma.doi)
        starturl = starturl + '/pdf'
    else:
        raise NoPDFLink('MISSING: pii, doi (doi lookup failed)')

    # Iter 1: do this until we see it stop working. (Iter 2: scrape download link from page.)
    return starturl.replace('/pdf', '/version/1/pdf/render')

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
        raise NoPDFLink('MISSING: pii, doi (doi lookup failed)') 

    try:
        r = requests.get(starturl)
    except requests.exceptions.TooManyRedirects:
        raise NoPDFLink('TXERROR: TooManyRedirects: cannot reach %s via %s' % (pma.journal, starturl))

    tree = etree.fromstring(r.text, HTMLParser())
    div = tree.cssselect('div.icon_pdf')[0]
    url = div.cssselect('a')[0].get('href')
    if url.find('.pdf') > -1:
        return url
    else:
        # give up, it's probably a "shopping cart" link.
        # TODO: parse return, raise more nuanced exceptions here.
        raise NoPDFLink('DENIED: cannot find pdf link (probably behind paywall)')

def the_biomed_calypso(pma):
    baseid = pma.doi if pma.doi else pma.pii
    if baseid:
        article_id = baseid.split('/')[1]
    else:
        raise NoPDFLink('MISSING: doi needed for BMC article')
    return BMC_format.format(aid=article_id)


def the_aaas_tango(pma):
    ja = aaas_journals[pma.journal]['ja']
    if pma.volume and pma.issue and pma.pages:
        pdfurl = aaas_format.format(ja=ja, a=pma)
    elif pma.doi:
        pdfurl = the_doi_2step(pma.doi) + '.full.pdf'
    else:
        raise NoPDFLink('MISSING: doi, vip (doi lookup failed)')

    response = requests.get(pdfurl)
    if response.status_code==200 and response.headers['content-type'].find('pdf') > -1:
        return response.url

    if response.status_code==200 and response.headers['content-type'].find('html') > -1:
        tree = etree.fromstring(response.content, HTMLParser())
        form = tree.cssselect('form')[1]
        fbi = form.fields.get('form_build_id')

        baseurl = urlsplit(response.url)
        post_url = baseurl.scheme + '://' + baseurl.hostname + form.action

        payload = { 'pass': AAAS_PASSWORD, 'name': AAAS_USERNAME, 'form_build_id': fbi, 'remember_me': 1 }
        response = requests.post(post_url, data=payload)
        if response.status_code==403:
            return AccessDenied('DENIED: AAAS subscription-only paper')
        elif response.headers['content-type'].find('pdf') > -1:
            return response.url
        elif response.headers['content-type'].find('html') > -1:
            raise NoPDFLink('DENIED: AAAS pdf download requires form navigation. URL: %s' % pdfurl)
    else:
        raise NoPDFLink('TXERROR: AAAS returned %s for url %s' % (response.status_code, pdfurl))


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
    raise NoPDFLink('DENIED: could not find PDF url in JAMA page (%s).' % url)

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
        raise NoPDFLink('TXERROR: %s did not resolve to jstage article' % url)

def the_wiley_shuffle(pma):
    '''  :param: pma (PubMedArticle object)
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    r = requests.get(format_templates['wiley'].format(a=pma))
    if r.headers['content-type'].find('html') > -1:
        if r.text.find('ACCESS DENIED') > -1:
            raise AccessDenied('DENIED: Wiley E Publisher says no to %s' % r.url)

        tree = etree.fromstring(r.text, HTMLParser())
        if tree.find('head/title').text.find('Not Found') > -1:
            raise NoPDFLink('TXERROR: Wiley says File Not found (%s)' % r.url)
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
        raise NoPDFLink('MISSING: pii, doi (doi lookup failed)')

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
            url = nature_format.format(a=pma, ja=nature_journals[pma.journal.translate(None, '.')]['ja'])
        else:
            if pma.doi:
                raise NoPDFLink('MISSING: pii, TXERROR: dx.doi.org resolution failed for doi %s' % pma.doi)
            else:
                raise NoPDFLink('MISSING: pii, doi')

    r = requests.get(url)
    if r.headers['content-type'].find('pdf') > -1:
        return r.url
    elif r.headers['content-type'].find('html') > -1:
        raise AccessDenied('DENIED: Nature denied access to %s' % r.url)
    raise NoPDFLink('TXERROR: unknown problem retrieving from %s' % r.url)

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
            raise NoPDFLink('TXERROR: could not get PDF url from either NIH or EuropePMC.org')

    if r.headers['content-type'].find('pdf') > -1:
        return url

    raise NoPDFLink('TXERROR: PMC download returned weird content-type %s' % r.headers['content-type'])


def the_springer_shag(pma):
    '''  :param: pma (PubMedArticle object)
         :return: url
         :raises: NoPDFLink
    '''
    # start: http://link.springer.com/article/10.1007%2Fs13238-015-0153-5
    # return: http://link.springer.com/content/pdf/10.1007%2Fs13238-015-0153-5.pdf
    if pma.doi:
        baseurl = the_doi_2step(pma.doi)
    else:
        raise NoPDFLink('MISSING: doi (doi lookup failed)')
    url = baseurl.replace('article', 'content/pdf') + '.pdf'
    r = requests.get(url)
    if not r.ok:
        raise NoPDFLink('TXERROR: %i status returned from Springer url (%s)' % (r.status_code, url))
    if r.headers['content-type'].find('pdf') > -1:
        return url
    else:
        raise AccessDenied('DENIED: Springer url (%s) resulted in HTTP %i' % (url, r.status_code))

