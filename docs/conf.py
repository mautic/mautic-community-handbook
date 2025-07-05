# Configuration file for the Sphinx documentation builder.

import sys, os
import sphinx_rtd_theme

sys.path.append(os.path.abspath('ext'))
sys.path.append('.')

from links.link import *
from links import *

# -- Project information

project = 'Mautic Community Handbook'
copyright = '2022, Mautic'
author = 'Mautic'

release = '0.1'
version = '0.1.0'

# -- General configuration

source_suffix = ['.rst', '.md']

extensions = [
    'xref',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'myst_parser'
]

myst_enable_extensions = [
    "linkify",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_static_path = ['css']

# -- Options for HTML output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Internationalisation configuration

locale_dirs = ['locale']

# Please add links here that do not pass the "make checklinks" check.
# A little context on the reason for ignoring is greatly appreciated!

linkcheck_ignore = [
      # Anchors are picked up as broken
    r"https://docs.mautic.org/policies/financial-policy#10-foreign-assets-control",
    r"https://github.com/abiosoft/colima?tab=readme-ov-file#installation",
    # The GitHub Search UI requires users to be authenticated with session cookies, which we can't set up programmatically
    r"https://github.com/search*",
    r"https://mau.tc/*",
    r"https://creativecommons.org/licenses/by-sa/3.0/legalcode",
    r"https://creativecommons.org/licenses/by-sa/3.0/",
    r"https://www.opensourcematters.org/organisation.html",
    r"https://www.drupal.org/governance",
]
