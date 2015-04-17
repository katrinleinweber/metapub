import glob, os

from setuptools import setup, find_packages
from metapub import __version__ as metapub_version

setup(
    name = 'metapub',
    version = metapub_version,
    description = 'Pubmed / NCBI / eutils interaction library, handling the metadata of pubmed papers.',
    url = 'https://bitbucket.org/nthmost/metapub',
    author = 'Naomi Most',
    maintainer = 'Naomi Most',
    author_email = 'naomi@nthmost.com',
    maintainer_email = 'naomi@nthmost.com',
    license = 'Apache 2.0',
    packages = find_packages(),
    install_requires = [
        'setuptools',
        'lxml',
        'requests',
        'eutils',
        'tabulate',
        'cssselect',
        ],
    )
