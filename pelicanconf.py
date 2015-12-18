# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'James Begley'
SITENAME = 'James Begley'
#SITEURL = 'http://jmbegley.github.io'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

THEME = 'pelican-bootstrap3'

GITHUB_USER = 'jmbegley'
GITHUB_SKIP_FORK = True
TWITTER_USERNAME = 'jmbegley'


# Feed generation is usually not desired when developing
#FEED_DOMAIN = 'http://jmbegley.github.io'
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# JMB
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
DISPLAY_BREADCRUMBS = True

DISPLAY_TAGS_ON_SIDEBAR = False

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/jmbegley'),
          ('facebook', 'http://www.facebook.com/jamesbegley'),
          ('linkedin', 'http://www.linkedin.com/in/jamesbegley'),
          ('github', 'http://github.com/jmbegley'),)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
