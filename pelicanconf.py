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
TWITTER_USERNAME = "isislovecruft"
#ARTICLE_URL = SITEURL'/{ slug }'
DEFAULT_CATEGORY = u'hacking' # if no "Category: " in post, use this
USE_FOLDER_AS_CATEGORY = True
NEWEST_FIRST_ARCHIVES = True
DISQUS_SITENAME = "patternsinthevoid"
#MENU_ITEMS = [
#    ('Hacking', os.path.join(SITENAME, 'category/hacking.html')),
#    ('Anarchism', os.path.join(SITENAME, 'category/anarchism.html')),
#    ('Physics', os.path.join(SITENAME, 'category/physics.html')),
#    ('Wandering', os.path.join(SITENAME, 'category/wandering.html')),
#    ]

# Dev settings:
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'published'

# Theme settings:
THEME = 'gazette'
THEME_STATIC_PATHS = ['static', 'images', 'prettify']
CSS_FILE = 'main.css' 
TYPOGRIFY = True
PRETTIFY = True

# Timezones, language, and metadata:
TIMEZONE = 'UTC'
DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs' # use filesystem metadata to get the creation date
DEFAULT_DATE_FORMAT = '%A, %d %B %Y'
# On Unix/Linux
DATE_FORMATS = {'en': ('en_US','%A, %d %B %Y'),}

#FEED_DOMAIN = SITEURL
FEED_RSS = u'feed.rss.xml'
FEED_RSS_ALL = u'all.rss.xml'
FEED_ATOM = u'feed.atom.xml'
FEED_ATOM_ALL = u'all.atom.xml'
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
FEED_MAX_ITEMS = 15

TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 10

# min articles on last page:
DEFAULT_ORPHANS = 2
# max per page (not including orphans):
DEFAULT_PAGINATION = 3
SUMMARY_MAX_LENGTH = 250

# Blogroll
LINKS =  (
    ('main', 'https://patternsinthevoid.net'),
    ('crypto', 'https://patternsinthevoid.net/isis.html'),
    ('contact', 'https://blog.patternsinthevoid.net/about.html'),
    ('projects', 'https://git.patternsinthevoid.net'),
    )
#    ('Image', 'https://image.patternsinthevoid.net'),
#    ('Sound', 'https://sound.patternsinthevoid.net'),

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/#!/isislovecruft'),
    ('Github', 'https://github.com/isislovecruft'),
    )
