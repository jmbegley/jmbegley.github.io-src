# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'James Begley'
SITENAME = 'James Begley'
SITEURL = 'http://www.jmbegley.org.uk'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'spacelab'

GITHUB_USER = 'jmbegley'
GITHUB_SKIP_FORK = True

TWITTER_USERNAME = 'jmbegley'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['tipue_search', 'filetime_from_git',
           'post_revision', 'feed_summary',
           'liquid_tags.img', 'liquid_tags.flickr']

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'http://www.jmbegley.org.uk'
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
DISPLAY_BREADCRUMBS = True

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['extras', 'images', 'files']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    }

#FAVICON = 'extras/favicon.ico'
#BANNER = 'extras/banner.jpg'
#CUSTOM_CSS = 'extras/custom.css'

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# share posts
SHARIFF = True
SHARIFF_LANG = "en"
SHARIFF_SERVICES  = "[&quot;facebook&quot;,&quot;googleplus&quot;,&quot;twitter&quot;]" #,&quot;mail&quot;]"
SHARIFF_THEME = "grey"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/jmbegley'),
          ('facebook', 'http://www.facebook.com/jamesbegley'),
          ('linkedin', 'http://www.linkedin.com/in/jamesbegley'),
          ('github', 'http://github.com/jmbegley'),
          ('email', 'mailto:james@jmbegley.org.uk', 'envelope'),)

DEFAULT_PAGINATION = 4

# post revision
GITHUB_URL = 'https://github.com/jmbegley/jmbegley.github.io-src'
POST_REVISION_TEXT = "Post History:"
POST_HISTORY_MAX_COUNT = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
