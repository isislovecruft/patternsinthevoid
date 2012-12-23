#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'https://patternsinthevoid.net/blog/'
SITENAME = 'Patterns in the Void'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'published'

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
#RELATIVE_URLS = False

#DISQUS_SITENAME = ""

SUMMARY_MAX_LENGTH = 50
DEFAULT_DATE = True
USE_FOLDER_AS_CATEGORY = True

TYPOGRIFY = True

ARTICLE_URL = '{SITEURL}/blog/{slug}'

# On Unix/Linux
DATE_FORMATS = {
    'en': ('en_US','%a, %d %b %Y'),
    }

FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = None
FEED_MAX_ITEMS = 15

# min articles on last page:
DEFAULT_ORPHANS = 2
DEFAULT_PAGINATION = 3

TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 100


