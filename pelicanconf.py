#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Patrick Allen'
SITENAME = 'patallen.me'
SITEURL = 'http://patallen.me'

PAGE_URL = 'pages/{slug}'
THEME = 'theme'

PATH = 'content'
# PROJECTS_PATH = 'content/projects' # We will use this for ProjectsGenerator

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
