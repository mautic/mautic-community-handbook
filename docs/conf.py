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

# GH Edit button

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "mautic",  # Username
    "github_repo": "mautic-community-handbook",  # Repository name
    "github_version": "main/",  # Branch name
    "conf_py_path": "/docs/",  # Path in the repository to conf.py
}

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
    # The GitHub Search UI requires users to be authenticated with session cookies, which we can't set up programmatically
    r"https://github.com/search*",
    r"https://mau.tc/*",
    r"https://creativecommons.org/licenses/by-sa/3.0/legalcode",
    r"https://creativecommons.org/licenses/by-sa/3.0/",
    r"https://www.opensourcematters.org/organisation.html",
    r"https://www.drupal.org/governance",
    r"https://github.com/mautic/mautic-community-handbook/blob/6956b3d3b4297735133717536d197c607c0bfa41/pages/04.community-leadership/02.leadership-role-definitions/docs.md#technical-community-lead",
    # Gitpod URLs often follow the pattern https://gitpod.io/#<repository_url>, which is not in the traditional sense for an HTML page
    r'https://gitpod\.io/.*',
    # The domain is blocking the link checker
    r'https://www.travel.dod.mil/Travel-Transportation-Rates/Per-Diem/Rate-Lookup/',
    # Frequent timeouts and errors when checking this link
    r"https://savannahcrm.com/public/*",
    # 403 errors from this domain
    r"https://www.glassdoor.co.uk/*",
    # 403 blocked errors
    r"https://www.drupal.org/governance/d8accelerate",
    # 403 client error
    r"https://www.canva.com/login/?redirect=%2Fdesign%2FDAFvp3RX9E4%2Ft7lTTciFvSBcdA_94XbTiQ%2Fview"
    # Ancor is picked up as not found
    r"https://docs.decidim.org/en/develop/admin/spaces/assemblies#_new_assembly_form"
    # Anchor is picked up as not found
    r"https://docs.decidim.org/en/develop/admin/components/meetings.html#_create_a_new_meeting"
    # Broken link due to anchor
    r"https://github.com/mautic/mautic/blob/8a57278758e2c3e1c1ca987aaf9ebd5f05b3c877/app/bundles/CampaignBundle/Executioner/Dispatcher/LegacyEventDispatcher.php#L201",
    # 403 errors from this domain
    r"https://www.drupal.org/about/core/policies/core-change-policies/drupal-deprecation-policy",
    # 403 errors from this domain
    r"https://pixabay.com",
    # 403 errors from this domain
    r"https://www.unsplash.com",
    # Anchor is picked up as not found
    r"https://github.com/mautic/mautic/blob/8a57278758e2c3e1c1ca987aaf9ebd5f05b3c877/app/bundles/CampaignBundle/Executioner/Dispatcher/LegacyEventDispatcher.php#L201",
    # 403 errors from this domain
    r"https://www.canva.com/*"
]
