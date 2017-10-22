#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import bulrush

AUTHOR = 'Ihfazhillah'
SITENAME = 'Ihfazhillah'
SITEURL = 'http://blog.ihfazh.com'

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'id'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('Facebook', 'https://facebook.com/mihfazhillah'),
          ('Github', 'https://github.com/ihfazhillah'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# extra path metadata
STATIC_PATHS = ['images', 'extra/CNAME', 'extra', 'statics']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
ARTICLE_EXCLUDES = ['statics']

# theme
THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS


# plugins PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']

DISQUS_SITENAME = "ihfazhillah"

DELETE_OUTPUT_DIRECTORY = True
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
