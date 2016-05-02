from __future__ import absolute_import, unicode_literals

import unicodedata

import six
from unidecode import unidecode

#py3k / py2k compatibility
if six.PY2:
    from urlparse import urlparse
else:
    from urllib.parse import urlparse

PUNCS_WE_DONT_LIKE = "[],.()<>'/?;:\"&"


def kpick(args, options, default=None):
    for opt in options:
        if args.get(opt, None):
            return args[opt]
    return default


def remove_chars(inp, chars=PUNCS_WE_DONT_LIKE):
    for char in chars:
        inp = inp.replace(char, '')
    return inp


def hostname_of(url):
    """ Takes a url (may or may not contain protocol prefix) and returns the simplest base form of the 
    hostname in the supplied URL.
    
    If hostname starts with 'www.', this will be stripped out.

    Examples: 
        http://www.nature.com/pr/journal/v49/n1/full/pr20018a.html --> nature.com
        https://webhome.weizmann.ac.il --> webhome.weizmann.ac.il
        http://www.ncbi.nlm.nih.gov/pubmed/17108762 --> ncbi.nlm.nih.gov

    :param url: (str)
    :return hostname: (str)
    """
    if url.startswith('http'):
        hostname = urlparse(url).hostname
    else:
        hostname = urlparse('http://' + url).hostname

    if hostname.startswith('www'):
        hostname = hostname.replace('www.', '')
    return hostname


def rootdomain_of(url):
    """ Returns the root domain of hostname of supplied URL. 

    Examples:
        http://blood.oxfordjournals.org --> oxfordjournals.org
        https://webhome.weizmann.ac.il --> ac.il
        https://regex101.com/ --> regex101.com
        http://www.ncbi.nlm.nih.gov/pubmed/17108762 --> nih.gov

    :param url: (str)
    :return rootdomain: (str)
    """
    hostname = hostname_of(url)
    return '.'.join(hostname.split('.')[-2:])


def asciify(inp):
    """ Nuke all the unicode from orbit. It's the only way to be sure.

    :param inp: (str)
    :return: string converted to pure, American ASCII
    """
    # TODO: be more diplomatic than an atomic bomb: convert international chars to ascii equivalents.
    # see http://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
    if inp:
        try:
            return inp.encode('ascii', 'ignore')
        except UnicodeDecodeError:
            return unicodedata.normalize('NFKD', inp.decode('utf-8')).encode('ascii', 'ignore')
    else:
        return ''


def squash_spaces(inp):
    """ Convert multiple ' ' chars to a single space.

    :param inp: (str)
    :return: same string with only one space where multiple spaces were.
    """
    return ' '.join(inp.split())


def parameterize(inp, sep='+'):
    """ Make strings suitable for submission to GET-based query service.

    Strips out the characters named in metapub.utils.PUNCS_WE_DONT_LIKE

    If inp is None, return empty string.

    :param inp: (str or None): input to be parameterized
    :param sep: (str): separator to use in place of spaces (default='+')
    :return: "parameterized" str
    """
    if inp is None:
        return ''

    inp = remove_chars(inp, PUNCS_WE_DONT_LIKE) 
    inp = squash_spaces(inp).replace(' ', sep)

    if six.PY2:
        return asciify(inp)
    else:
        return unidecode(inp)


def deparameterize(inp, sep='+'):
    """ Somewhat-undo parameterization in string. Replace separators (sep) with spaces.

    :param inp: (str)
    :param sep: (str) default: '+'
    :return: "deparameterized" string
    """
    return inp.replace(sep, ' ')


def remove_html_markup(inp):
    """ Remove html and xml tags from text.
    Preserves HTML entities like &amp;

    :param inp: (str)
    :return: string with HTML and XML markup removed.
    """
    tag = False
    quote = False
    out = ""

    for char in inp:
        if char == '<' and not quote:
            tag = True
        elif char == '>' and not quote:
            tag = False
        elif (char == '"' or char == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + char
    return out


def lowercase_keys(dct):
    """ Takes an input dictionary, returns dictionary with all keys lowercased. """
    result = {}
    for key, value in list(dct.items()):
        result[key.lower()] = value
    return result
