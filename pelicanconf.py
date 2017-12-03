#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ihfazhillah'
SITENAME = 'Ihfazhillah'
ABOUTME_SUMMARY = "Software Developer. Bagian IT di Yayasan <a href='http://ussunnah.org'>Us Sunnah</a>. Menulis code menggunakan javascript dan python. Ayah dari 2 anak yang lucu, Alhamdulillah."
EMAIL = 'mihfazhillah@gmail.com'
PHONE = '(+62) 823-1371-8759'
ADDRESS = 'Kradenan Rt 2/6, Tingkir Lor Tingkir Salatiga'
#SITEURL = 'http://blog.ihfazh.com'

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
SOCIAL = (('facebook', 'https://facebook.com/mihfazhillah'),
          ('github', 'https://github.com/ihfazhillah'),
          ('linkedin', 'https://www.linkedin.com/in/ihfazhillah/')
          )

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# extra path metadata
STATIC_PATHS = ['images', 'extra/CNAME', 'extra', 'statics']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
ARTICLE_EXCLUDES = ['statics']

# theme
#THEME = bulrush.PATH
#JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
#JINJA_FILTERS = bulrush.FILTERS
THEME = "themes/editorial"

# plugins PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['assets']

DISQUS_SITENAME = "ihfazhillah"

# DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = False
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
