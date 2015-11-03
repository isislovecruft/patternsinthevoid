#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys
sys.path.append('.')

topdir = os.getcwd()

# Dev settings:
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'output'

# Publish settings:
#DELETE_OUTPUT_DIRECTORY = False
# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = True

# Basic settings
#################

AUTHOR = u'Isis Agora Lovecruft'
SITENAME = u'Patterns in the Void'
SITEURL = 'https://blog.patternsinthevoid.net'
FEED_DOMAIN = 'https://blog.patternsinthevoid.net'
GITHUB_URL = 'https://github.com/isislovecruft'
TWITTER_USERNAME = "isislovecruft"
ALLOW_TWITTER_SHARE = False
FLATTR = True

# Article Settings
###################

#ARTICLE_URL = SITEURL'/{ slug }'
DEFAULT_CATEGORY = u'hacking' # if no "Category:" in post, use this
USE_FOLDER_AS_CATEGORY = True
NEWEST_FIRST_ARCHIVES = True
#MENU_ITEMS = [
#    ('Hacking', os.path.join(SITENAME, 'category/hacking.html')),
#    ('Anarchism', os.path.join(SITENAME, 'category/anarchism.html')),
#    ('Physics', os.path.join(SITENAME, 'category/physics.html')),
#    ('Wandering', os.path.join(SITENAME, 'category/wandering.html')),
#    ]

# Theme settings
#################

THEME = 'gazette'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'
TYPOGRIFY = True
PRETTIFY = True

FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),
                 ('extra/favicon.ico', 'favicon.ico'),)

from plugins import neighbors
from plugins import pelican_bibtex as bibtex
from plugins import summary
from plugins import clean_summary
from plugins import representative_image

PLUGINS = [
    neighbors,
    bibtex,
    summary,
    clean_summary,
    representative_image,
]

DIRECT_TEMPLATES = ('index', 'libris', 'tags', 'categories', 'archives', 'sitemap')
PAGINATED_DIRECT_TEMPLATES = ('index',)
SITEMAP_SAVE_AS = 'sitemap.xml'

## Maximum number of images to include in an article summary:
CLEAN_SUMMARY_MAXIMUM = 3
## If True, try to include at least one image in each article summary:
CLEAN_SUMMARY_MINIMUM_ONE = True

## Whether to include a flashproxy and CC license in the footer:
FLASHPROXY = True
DISPLAY_CC = True

## These show up as 'http(s)://<SITE_URL>/static/libris/'
STATIC_PATHS = ['images', 'pages', 'libris']
## The following disables showing "About the author" on the menu
DISPLAY_PAGES_ON_MENU = False

# BIBTEX PUBLICATIONS
####################################
PUBLICATIONS_SRC = 'content/libris/atricoloris.bib'

# Timezones, language, and metadata
####################################
TIMEZONE = 'UTC'
DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs' # use filesystem metadata to get the creation date
DEFAULT_DATE_FORMAT = '%A, %d %B %Y'
DATE_FORMATS = {'en_US': ('en_US','%A, %d %B %Y'),}

#FEED_DOMAIN = SITEURL
FEED_RSS = u'feed.rss.xml'
FEED_RSS_ALL = u'all.rss.xml'
FEED_ATOM = u'feed.atom.xml'
FEED_ATOM_ALL = u'all.atom.xml'
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
FEED_MAX_ITEMS = 15

TAG_CLOUD_STEPS = 0
TAG_CLOUD_MAX_ITEMS = 0

# min articles on last page:
DEFAULT_ORPHANS = 2
# max per page (not including orphans):
DEFAULT_PAGINATION = 3
SUMMARY_MAX_LENGTH = 500

# Blogroll
LINKS =  (
    ('pelagus', 'https://fyb.patternsinthevoid.net'),
    ('clavium apertum', 'https://blog.patternsinthevoid.net/isis.txt'),
    ('codii et codicilli', 'https://code.patternsinthevoid.net'),
    #('horologii', 'https://blog.patternsinthevoid.net/calendar.html'),
    ('elogii biothanatum', 'https://blog.patternsinthevoid.net/pages/about-the-author.html'),
    ('libris atricoloris', 'https://blog.patternsinthevoid.net/pages/libris.html'),
    ('imaginis', 'https://blog.patternsinthevoid.net/static/images'),
    #('strepitus', 'https://sound.patternsinthevoid.net')
    )
SOCIAL = (
    ('twitter', 'https://twitter.com/isislovecruft'),
    ('github', 'https://github.com/isislovecruft'),
    #('flattr this!', 'https://flattr.com/submit/auto?user_id=isislovecruft&url=https://blog.patternsinthevoid.net/index.html'),
    #('#tor-status', 'https://gs.torproject.org/person/isis'),
)
