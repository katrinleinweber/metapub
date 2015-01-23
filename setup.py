import glob, os

from setuptools import setup, find_packages

setup(
    name = 'metapub',
    version = '0.2.1',
    description = 'Pubmed / NCBI / eutils interaction library, handling the metadata of pubmed papers.',
    url = 'https://bitbucket.org/nthmost/metapub',
    author = 'Naomi Most',
    maintainer = 'Naomi Most',
    author_email = 'naomi@nthmost.com',
    maintainer_email = 'naomi@nthmost.com',
    license = 'Apache 2.0',
    packages = find_packages(),
    setup_request = [ 'hgtools', 'pytz' ],
    install_requires = [
        'setuptools',
        'lxml',
        'requests',
        'eutils',
        'tabulate',
        ],
    )
