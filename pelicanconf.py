#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Louie Dinh'
SITENAME = u'Python Practice Projects'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Good to Great', 'http://jessenoller.com/good-to-great-python-reads/'),
         ('Charming Python', 'http://gnosis.cx/publish/tech_index_cp.html'),
         ('PEP8', 'http://www.python.org/dev/peps/pep-0008/'),
         ('Hitchhiker\'s Guide', 'http://docs.python-guide.org/en/latest/'),
         ('Python Weekly', 'http://www.pythonweekly.com/'))

# Social widget
SOCIAL = {'twitter': 'http://twitter.com/louiedinh',
          'linkedin': 'http://www.linkedin.com/profile/view?id=103017614'}

DEFAULT_PAGINATION = False

THEME = 'themes/built-texts'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

INDEX_SAVE_AS = 'blog.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

GOOGLE_ANALYTICS = 'UA-39716444-2'
TWITTER_USERNAME = "louiedinh"
DISQUS_SITENAME = "pythonpracticeprojects"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_EXCLUDES = ('pages', 'drafts')

EMAIL_SUBSCRIBE_URL = "http://www.eepurl.com/FnX4f"
FORUMS_URL = "http://discourse.pythonpracticeprojects.com"
BUY_URL = "https://gumroad.com/l/cSIzC"

SITE_META_DESCRIPTION = "Programming practice projects designed to take your Python coding chops to the next level"

