from __future__ import absolute_import, print_function

__author__ = 'nthmost'

import sys

from urlparse import urlsplit

import requests
from lxml.html import HTMLParser
from lxml import etree

from ..pubmedarticle import square_voliss_data_for_pma
from ..exceptions import AccessDenied, NoPDFLink
from ..text_mining import find_doi_in_string
from ..utils import asciify

from .journals import *

OK_STATUS_CODES = (200, 301, 302, 307)

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
        raise NoPDFLink('dx.doi.org lookup failed for doi %s (HTTP %i returned)' %
                        (doi, response.status_code))

def standardize_journal_name(journal_name):
    '''protect against unicode character mishaps in journal names.

    Returns a "standardized" journal name with periods stripped out.'''
    # (did you know that unicode.translate takes ONE argument whilst
    #   str.translate takes TWO?! true story)
    return asciify(journal_name).translate(None, '.')

def verify_pdf_url(pdfurl, publisher_name=''):
    res = requests.get(pdfurl)
    if res.status_code==401:
        raise NoPDFLink('DENIED: %s url (%s) requires login.' % (publisher_name, pdfurl))

    if not res.ok:
        raise NoPDFLink('TXERROR: %i status returned from %s url (%s)' % (res.status_code, 
                            publisher_name, pdfurl))

    if res.status_code in OK_STATUS_CODES and res.headers['content-type'].find('pdf') > -1:
        return pdfurl
    else:
        raise NoPDFLink('DENIED: %s url (%s) did not result in a PDF' % (publisher_name, pdfurl))

def rectify_pma_for_vip_links(pma):
    '''takes a PubMedArticle object and "squares" the volume/issue/page info (sometimes there
    are weird characters in it, or sometimes the issue number is packed into the volume field,
    stuff like that).

    If volume, issue, and page data are all represented, return the PubMedArticle (possibly
    modified).

    If missing data, raise NoPDFLink('MISSING: vip...') 
    '''
    pma = square_voliss_data_for_pma(pma)
    if pma.volume and pma.first_page and pma.issue:
        return pma
    raise NoPDFLink('MISSING: vip (volume, issue, and/or first_page missing from PubMedArticle)')

def the_doi_slide(pma, verify=True):
    '''Dance of the miscellaneous journals that use DOI in their URL construction.

         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    jrnl = asciify(pma.journal).translate(None, '.')
    if pma.doi:
        url = simple_formats_doi[jrnl].format(a=pma)
    else:
        raise NoPDFLink('MISSING: doi (lookup failed)')

    if verify:
        verify_pdf_url(url)
    return url

def the_pmid_pogo(pma, verify=True):
    '''Dance of the miscellaneous journals that use PMID in their URL construction.

         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    jrnl = standardize_journal_name(pma.journal)
    url = simple_formats_pmid[jrnl].format(pmid=pma.pmid)

    if verify:
        verify_pdf_url(url)
    return url

def the_vip_shake(pma, verify=True):
    '''Dance of the miscellaneous journals that use volume-issue-page in their
        URL construction

         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    jrnl = standardize_journal_name(pma.journal)
    pma = rectify_pma_for_vip_links(pma)  #raises NoPDFLink if missing data.
    url = vip_format.format(host=vip_journals[jrnl]['host'], a=pma)

    if verify:
        verify_pdf_url(url)
    return url

def the_vip_nonstandard_shake(pma, verify=True):
    '''Dance of the miscellaneous journals that use volume-issue-page in their
        URL construction (but are a little different).

         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    jrnl = standardize_journal_name(pma.journal)
    pma = rectify_pma_for_vip_links(pma)  #raises NoPDFLink if missing data.
    url = vip_journals_nonstandard[jrnl].format(a=pma)

    if verify:
        verify_pdf_url(url)
    return url
 

def the_pii_polka(pma, verify=True):
    '''Dance of the miscellaneous journals that use a PII in their URL construction
        in their URL construction.

         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    jrnl = standardize_journal_name(pma.journal)
    if pma.pii:
        url = simple_formats_pii[jrnl].format(a=pma)
    else:
        raise NoPDFLink('MISSING: pii missing from PubMedArticle XML (pii format)')

    if url:
        res = requests.get(url)
        if res.text.find('Access Denial') > -1:
            raise AccessDenied('DENIED: Access Denied by ScienceDirect (%s)' % url)

    if verify:
        verify_pdf_url(url)
    return url


def the_jci_jig(pma, verify=True):
    '''Dance of the Journal of Clinical Investigation, which should be largely free.

         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    # approach: pii with dx.doi.org fallback to get pdf "view" page; scrape pdf download link.
    if pma.pii:
        starturl = doi_templates['jci'].format(a=pma)
    elif pma.doi:
        starturl = the_doi_2step(pma.doi)
        starturl = starturl + '/pdf'
    else:
        raise NoPDFLink('MISSING: pii, doi (doi lookup failed)')

    # Iter 1: do this until we see it stop working. (Iter 2: scrape download link from page.)
    url = starturl.replace('/pdf', '/version/1/pdf/render')
    if verify:
        verify_pdf_url(url, 'JCI')
    return url

def the_najms_mazurka(pma, verify=True):
    '''Dance of the North Am J Med Sci, which should be largely free.

         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    # approach: the_doi_2step, scrape for PDF link.

    #PDF link looks like this:
    #http://www.najms.org/downloadpdf.asp?issn=1947-2714;year=2012;volume=4;issue=10;spage=435;epage=441;aulast=Andr%E9n-Sandberg;type=2

    if pma.doi:
        starturl = the_doi_2step(pma.doi)
    else:
        raise NoPDFLink('MISSING: pii, doi (doi lookup failed)')
    #response = requests.get(starturl)
    #if not response.content.find('downloadpdf.asp') > -1:
    #    raise NoPDFLink('DENIED: no PDF link in page.')
    
    raise NotImplementedError('NOFORMAT: NAJMS support incomplete; see metapub.findit.dances.the_najms_mazurka')

    if verify:
        verify_pdf_url(url, 'NAJMS')
    return url

def the_sciencedirect_disco(pma, verify=True):
    '''Note: verify=True required to find link.  Parameter supplied only for unity 
       with other dances.

         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    #we're looking for a url that looks like this:
    #http://www.sciencedirect.com/science/article/pii/S0022283601953379/pdfft?md5=07db9e1b612f64ea74872842e34316a5&pid=1-s2.0-S0022283601953379-main.pdf

    starturl = None
    if pma.pii:
        starturl = sciencedirect_url.format(piit=pma.pii.translate(None, '-()'))
    elif pma.doi:
        starturl = the_doi_2step(pma.doi)

    if starturl == None:
        raise NoPDFLink('MISSING: pii, doi (doi lookup failed)')

    try:
        res = requests.get(starturl)
    except requests.exceptions.TooManyRedirects:
        raise NoPDFLink('TXERROR: ScienceDirect TooManyRedirects: cannot reach %s via %s' %
                        (pma.journal, starturl))

    tree = etree.fromstring(res.text, HTMLParser())
    try:
        div = tree.cssselect('div.icon_pdf')[0]
    except IndexError:
        raise NoPDFLink('DENIED: ScienceDirect did not provide pdf link (probably paywalled)')
    url = div.cssselect('a')[0].get('href')
    if url.find('.pdf') > -1:
        return url
    else:
        # give up, it's probably a "shopping cart" link.
        raise NoPDFLink('DENIED: ScienceDirect did not provide pdf link (probably paywalled)')

def the_biomed_calypso(pma, verify=False):
    '''Note: verification turned off by default because BMC is an all-open-access publisher.

       (You may still like to use verify=True to make sure it's a valid link.)

         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: False]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    baseid = pma.doi if pma.doi else pma.pii
    if baseid:
        article_id = baseid.split('/')[1]
    else:
        raise NoPDFLink('MISSING: doi needed for BMC article')
    url = BMC_format.format(aid=article_id)
    if verify:
        verify_pdf_url(url, 'BMC')
    return url


def the_aaas_tango(pma, verify=True):
    '''Note: "verify" param recommended here (page navigation usually necessary).
    
         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    #try:
    #    pma = rectify_pma_for_vip_links(pma)
    #    pdfurl = aaas_format.format(ja=aaas_journals[pma.journal]['ja'], a=pma)
    #except NoPDFLink:
        # try the pmid-based approach
    baseurl = 'http://www.sciencemag.org/cgi/pmidlookup?view=long&pmid=%s' % pma.pmid
    res = requests.get(baseurl)
    pdfurl = res.url.replace('.long', '.full') + '.pdf'

    if not verify:
        return pdfurl

    response = requests.get(pdfurl)
    if response.status_code == 200 and response.headers['content-type'].find('pdf') > -1:
        return response.url

    elif response.status_code == 200 and response.headers['content-type'].find('html') > -1:
        tree = etree.fromstring(response.content, HTMLParser())

        if not tree.find('head/title').text.find('Sign In') > -1:
            raise NoPDFLink('TXERROR: AAAS returned unexpected HTML response for url %s' % (pdfurl))
        else:
            # some items are acquirable via free account registration... but let's not mess with this just yet.
            raise NoPDFLink('DENIED: AAAS paper subscription-only or requires site registration (url: %s)' % pdfurl)
    
        form = tree.cssselect('form')[0]
        fbi = form.fields.get('form_build_id')

        baseurl = urlsplit(response.url)
        post_url = baseurl.scheme + '://' + baseurl.hostname + form.action

        payload = {'pass': AAAS_PASSWORD, 'name': AAAS_USERNAME,
                   'form_build_id': fbi, 'remember_me': 1}
        print("SUBMITTING TO AAAS")
        print(payload)

        response = requests.post(post_url, data=payload)
        if response.status_code == 403:
            return AccessDenied('DENIED: AAAS subscription-only paper (url: %s)')
        elif response.headers['content-type'].find('pdf') > -1:
            return response.url
        elif response.headers['content-type'].find('html') > -1:
            #if response.content.find('access-denied') > -1:
            raise NoPDFLink('DENIED: AAAS subscription-only paper (url: %s)' % pdfurl)
    else:
        raise NoPDFLink('TXERROR: AAAS returned %s for url %s' % (response.status_code, pdfurl))

def the_jama_dance(pma, verify=True):
    '''  :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''

    baseurl = the_doi_2step(pma.doi)
    res = requests.get(baseurl)
    parser = HTMLParser()
    tree = etree.fromstring(res.text, parser)
    # we're looking for a meta tag like this:
    # <meta name="citation_pdf_url" content="http://archneur.jamanetwork.com/data/Journals/NEUR/13776/NOC40008.pdf" />
    for item in tree.findall('head/meta'):
        if item.get('name') == 'citation_pdf_url':
            pdfurl = item.get('content')
        else:
            raise NoPDFLink('DENIED: JAMA did not provide PDF link in (%s).' % baseurl)
    if verify:
        #TODO: form navigation
        verify_pdf_url(pdfurl, 'JAMA')
    return pdfurl

def the_jstage_dive(pma, verify=True):
    '''  :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    if pma.doi:
        url = the_doi_2step(pma.doi)
        res = requests.get(url)
        if res.url.find('jstage') > -1:
            url = res.url.replace('_article', '_pdf')
            pdfpos = url.find('_pdf')
            # remove everything after the "_pdf" part
            url = url[:pdfpos+4]
    else:
        raise NoPDFLink('MISSING: doi for dx.doi.org lookup to get jstage link')

    if verify:
        verify_pdf_url(url, 'jstage')
    return url


def the_wiley_shuffle(pma, verify=True):
    '''Returns a PDF link to an article from a Wiley-published journal.

    Note: Wiley sometimes buries PDF links in HTML pages we have to parse first.
    Turning off verification (verify=False) may return only a superficial link.
         
         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    url = doi_templates['wiley'].format(a=pma)
    if not verify:
        return url

    # wiley sometimes buries PDF links in HTML pages we have to parse.
    res = requests.get(url)
    if res.headers['content-type'].find('html') > -1:
        if res.text.find('ACCESS DENIED') > -1:
            raise AccessDenied('DENIED: Wiley E Publisher says no to %s' % res.url)

        tree = etree.fromstring(res.text, HTMLParser())
        if tree.find('head/title').text.find('Not Found') > -1:
            raise NoPDFLink('TXERROR: Wiley says File Not found (%s)' % res.url)
        elif tree.find('head/title').text.find('Maintenance') > -1:
            raise NoPDFLink('TXERROR: Wiley site under scheduled maintenance -- try again later (url was %s).' % res.url)
        iframe = tree.find('body/div/iframe')
        url = iframe.get('src')
        verify_pdf_url(url, 'Wiley')
        return url

    elif res.headers['content-type'].find('pdf' > -1):
        return res.url


def the_lancet_tango(pma, verify=True):
    '''  :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url (string)
         :raises: AccessDenied, NoPDFLink
    '''
    if pma.pii:
        url = doi_templates['lancet'].format(a=pma, ja=lancet_journals[pma.journal.translate(None, '.')]['ja'])
    if pma.doi:
        url = the_doi_2step(pma.doi).replace('abstract', 'pdf').replace('article', 'pdfs')
    else:
        raise NoPDFLink('MISSING: pii, doi (doi lookup failed)')
    
    if verify:
        verify_pdf_url(url, 'Lancet')
    return url

def the_nature_ballet(pma, verify=True):
    '''  :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
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

    if url == '':
        if pma.pii:
            url = nature_format.format(a=pma, ja=nature_journals[pma.journal.translate(None, '.')]['ja'])
        else:
            if pma.doi:
                raise NoPDFLink('MISSING: pii, TXERROR: dx.doi.org resolution failed for doi %s' % pma.doi)
            else:
                raise NoPDFLink('MISSING: pii, doi')

    if verify:
        verify_pdf_url(url, 'Nature')
    return url


PMC_PDF_URL = 'http://www.ncbi.nlm.nih.gov/pmc/articles/pmid/{a.pmid}/pdf'
EUROPEPMC_PDF_URL = 'http://europepmc.org/backend/ptpmcrender.fcgi?accid=PMC{a.pmc}&blobtype=pdf'
def the_pmc_twist(pma, verify=True, use_nih=False):
    '''Look up article in EuropePMC.org.  If not found there, fall back to NIH (if use_nih
    is True).

       Note: verification highly recommended. EuropePMC has most articles, but not everything.

         :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :param: use_nih (bool) [default: False]
         :return: url
         :raises: NoPDFLink
    '''
    if pma.history.get('pmc-release', None):
        # marked "PAYWALL" here because FindIt will automatically retry such cached entries
        raise NoPDFLink('PAYWALL: pmc article in embargo until %s' % pma.history['pmc-release'].strftime('%Y-%m-%d'))

    url = EUROPEPMC_PDF_URL.format(a=pma)

    if not verify:
        return url

    try:
        verify_pdf_url(url, 'EuropePMC')
        return url

    except (NoPDFLink, AccessDenied):
        # Fallback to using NIH.gov if we're allowing it.        
        if use_nih:
            #   URL block might be discerned by grepping for this:
            #
            #   <div class="el-exception-reason">Bulk downloading of content by IP address [162.217...,</div>
            url = PMC_PDF_URL.format(a=pma)
            verify_pdf_url(url, 'NIH (EuropePMC fallback)')
            return url
    raise NoPDFLink('TXERROR: could not get PDF from EuropePMC.org and USE_NIH set to False')


def the_springer_shag(pma, verify=True):
    '''  :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url
         :raises: AccessDenied, NoPDFLink
    '''
    # start: http://link.springer.com/article/10.1007%2Fs13238-015-0153-5
    # return: http://link.springer.com/content/pdf/10.1007%2Fs13238-015-0153-5.pdf
    if pma.doi:
        baseurl = the_doi_2step(pma.doi)
    else:
        raise NoPDFLink('MISSING: doi (doi lookup failed)')
    url = baseurl.replace('article', 'content/pdf') + '.pdf'

    if verify:
        verify_pdf_url(url, 'Springer')
    return url

def the_karger_conga(pma, verify=True):
    '''  :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url
         :raises: AccessDenied, NoPDFLink
    '''
    # example: 23970213.  doi = 10.1159/000351538
    #       http://www.karger.com/Article/FullText/351538
    #       http://www.karger.com/Article/Pdf/351538

    if pma.doi: 
        if find_doi_in_string(pma.doi):
            kid = pma.doi.split('/')[1]
            if kid.isdigit():
                kid = str(int(kid))     # strips the zeroes that are padding the ID in the front.
        else:
            kid = pma.doi
            # sometimes the Karger ID was put in as the DOI (e.g. pmid 11509830)
        baseurl = 'http://www.karger.com/Article/FullText/%s' % kid
    else:
        raise NoPDFLink('MISSING: doi (doi lookup failed)')
    # if it directs to an "Abstract", we prolly can't get the PDF. Try anyway.
    url = baseurl.replace('FullText', 'Pdf').replace('Abstract', 'Pdf')

    if verify:
        verify_pdf_url(url, 'Karger')
    return url


def the_spandidos_lambada(pma, verify=True):
    '''  :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url
         :raises: AccessDenied, NoPDFLink
    '''
    jrnl = standardize_journal_name(pma.journal)
    baseurl = None
    try:
        pma = rectify_pma_for_vip_links(pma)  #raises NoPDFLink if missing data
        url = spandidos_format.format(ja=spandidos_journals[jrnl]['ja'], a=pma)
    except NoPDFLink:
        # let doi2step exceptions fall to calling function
        if pma.doi:
            baseurl = the_doi_2step(pma.doi)
            url = baseurl + '/download'
        else:
            raise NoPDFLink('MISSING: vip, doi - volume and/or issue missing from PubMedArticle; doi lookup failed.')

    if verify:
        verify_pdf_url(url, 'Spandidos')
    return url


def the_wolterskluwer_volta(pma, verify=True):
    '''  :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url
         :raises: AccessDenied, NoPDFLink
    '''
    doiurl = 'http://content.wkhealth.com/linkback/openurl?doi=%s'
    volissurl = 'http://content.wkhealth.com/linkback/openurl?issn={a.issn}&volume={a.volume}&issue={a.issue}&spage={a.first_page}'
    if pma.doi:
        baseurl = requests.get(doiurl % pma.doi).url
    elif pma.issn:
        pma = rectify_pma_for_vip_links(pma)  #raises NoPDFLink if missing data
        baseurl = requests.get(volissurl.format(a=pma)).url
        
    res = requests.get(baseurl)
    tree = etree.fromstring(res.text, HTMLParser())
    try:
        item = tree.cssselect('li.ej-box-01-body-li-article-tools-pdf')[0]
    except IndexError:
        raise NoPDFLink('DENIED: wolterskluwer did not provide PDF link for this article')
    link = item.getchildren()[0]
    url = link.get('href')
    if verify:
        verify_pdf_url(url)
    return url


def the_biochemsoc_saunter(pma, verify=True):
    '''  :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url
         :raises: AccessDenied, NoPDFLink
    '''
    jrnl = standardize_journal_name(pma.journal)
    pma = rectify_pma_for_vip_links(pma)  #raises NoPDFLink if missing data 
    host = biochemsoc_journals[jrnl]['host']
    url = biochemsoc_format.format(a=pma, host=host, ja=biochemsoc_journals[jrnl]['ja'])
    if verify:
        verify_pdf_url(url, 'biochemsoc')
    return url

def the_cell_pogo(pma, verify=True):
    '''  :param: pma (PubMedArticle object)
         :param: verify (bool) [default: True]
         :return: url
         :raises: AccessDenied, NoPDFLink
    '''
    jrnl = standardize_journal_name(pma.journal)
    if pma.pii:
        # the front door
        url = cell_format.format(a=pma, ja=cell_journals[jrnl]['ja'],
                                     pii=pma.pii.translate(None, '-()'))
        if verify:
            verify_pdf_url(url, 'Cell')
        return url
    else:
        # let the SD function raise Exceptions
        return the_sciencedirect_disco(pma, verify)

