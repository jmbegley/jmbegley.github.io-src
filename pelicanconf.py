# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'James Begley'
SITENAME = 'Random Thoughts From the Edge of Mendipshire'
#SITEURL = 'https://www.jmbegley.org.uk'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

THEME = 'pelican-plugins/pelican-bootstrap3'
BOOTSTRAP_THEME = 'lumen'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

#GITHUB_USER = 'jmbegley'
#GITHUB_SKIP_FORK = True

TWITTER_USERNAME = 'jmbegley'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['tipue_search', 'filetime_from_git',
           'post_revision', 'i18n_subsites',
           'liquid_tags.img', 'liquid_tags.flickr']

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pygment highlighting scheme
PYGMENTS_STYLE = 'solarizeddark'

SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
DISPLAY_BREADCRUMBS = True

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['extras', 'files', 'images']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    }

FAVICON = 'extras/favicon.ico'
#BANNER = 'extras/banner.jpg'
#CUSTOM_CSS = 'extras/custom.css'

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# share posts
SHARIFF = True
SHARIFF_LANG = "en"
SHARIFF_SERVICES  = "[&quot;twitter&quot;,&quot;facebook&quot;,&quot;linkedin&quot;,&quot;whatsapp&quot;]"#,&quot;print&quot;,&quot;mail&quot;]"
SHARIFF_THEME = "standard"
SHARIFF_ORIENTATION = "horizontal"

# Blogroll
LINKS = (('Mendip Cave Rescue', 'https://www.mendipcaverescue.org/'),
         ('Shepton Mallet Caving Club', 'https://www.shepton.org.uk/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/jmbegley'),
          ('facebook', 'https://www.facebook.com/jamesbegley'),
          ('linkedin', 'https://www.linkedin.com/in/jamesbegley'),
          ('github', 'https://github.com/jmbegley'),
          ('flickr', 'https://www.flickr.com/photos/jmbegley'),
#         ('strava', 'https://www.strava.com/athletes/7460696'),
          ('rss', SITEURL + '/' + FEED_ALL_ATOM),
          ('email', 'mailto:james@jmbegley.org.uk', 'envelope'),)

DEFAULT_PAGINATION = 4

# post revision
GITHUB_URL = 'https://github.com/jmbegley/jmbegley.github.io-src'
POST_REVISION_TEXT = "Post History:"
POST_HISTORY_MAX_COUNT = 3

# about me
SHOW_ABOUTME = True
AVATAR = "images/jmb.jpg"
ABOUT_ME = """
I work with computers, usually analysing problems to see why things aren't working as expected.
<br/><br/>
My other interests include caving, skiing, running and cooking.
"""

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
