#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys
sys.path.append('.')

topdir = os.getcwd()

AUTHOR = u'Isis Agora Lovecruft'
SITENAME = u'Patterns in the Void'
SITEURL = 'https://blog.patternsinthevoid.net'
GITHUB_URL = 'https://github.com/isislovecruft'
#ARTICLE_URL = '{ SITEURL }/{ slug }'
DEFAULT_CATEGORY = u'/dev/random' # if no "Category: " in post, use this
USE_FOLDER_AS_CATEGORY = True

# Dev settings:
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'published'

# Theme settings:
THEME = './newspaper-theme/'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css' 
TYPOGRIFY = True

# Timezones, language, and metadata:
TIMEZONE = 'UTC'
DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs' # use filesystem metadata to get the creation date
DEFAULT_DATE_FORMAT = '%A, %d %B %Y'
# On Unix/Linux
DATE_FORMATS = {'en': ('en_US','%A, %d %B %Y'),}

FEED_DOMAIN = SITEURL
FEED_RSS = u'feed.rss.xml'
FEED_RSS_ALL = u'all.rss.xml'
FEED_ATOM = u'feed.atom.xml'
FEED_ATOM_ALL = u'all.atom.xml'
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
FEED_MAX_ITEMS = 15

TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 100

# min articles on last page:
DEFAULT_ORPHANS = 2
# max per page (not including orphans):
DEFAULT_PAGINATION = 3
SUMMARY_MAX_LENGTH = 50

# Blogroll
LINKS =  (
    ('Home', 'https://patternsinthevoid.net'),
    ('Crypto', 'https://patternsinthevoid.net/isis'),
    ('Code', 'https://code.patternsinthevoid.net'),
    ('Image', 'https://image.patternsinthevoid.net'),
    ('Sound', 'https://sound.patternsinthevoid.net'),
    ('Jinja2', 'http://jinja.pocoo.org'),
    )

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/#!/isislovecruft'),
    ('Github', 'https://github.com/isislovecruft'),
    ('Another social link', '#'),
    )
