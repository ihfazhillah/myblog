#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Ihfazhillah'
SITENAME = 'Ihfazhillah'
ABOUTME_SUMMARY = "Teacher and a Software developer. Working with python, and javascript. Freelancer and a coffe addict"
EMAIL = 'mihfazhillah@gmail.com'
PHONE = '(+62) 823-1371-8759'
ADDRESS = 'Kradenan Rt 2/6, Tingkir Lor Tingkir Salatiga'
SITEURL = 'https://blog.ihfazh.com'

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'id'

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (('facebook', 'https://facebook.com/mihfazhillah'),
          ('github', 'https://github.com/ihfazhillah'),
          ('linkedin', 'https://www.linkedin.com/in/ihfazhillah/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# extra path metadata
STATIC_PATHS = ['images', 'extra/CNAME', 'extra', 'statics']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {
        'path': 'CNAME'
    },
}
ARTICLE_EXCLUDES = ['statics']

# theme
THEME = "themes/minimalxy"

# plugins PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['assets']

GOOGLE_ANALYTICS = "UA-117778347-1"
DISQUS_SITENAME = "ihfazhillah"

MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
ARCHIVES_SAVE_AS = 'archives.html'
CATEGORIES_SAVE_AS = 'categories.html'

MINIMALXY_START_YEAR = 2013
MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Assalamualaykum, I`m Ihfazhillah. Here\'s some thoughts of mine'
AUTHOR_DESCRIPTION = u'Teacher and Software developer. Working mostly with python. You can say I\'m a fullstack developer.'
AUTHOR_AVATAR = 'https://avatars3.githubusercontent.com/u/13466064?s=460&v=4.png'
AUTHOR_WEB = 'https://blog.ihfazh.com'

MENUITEMS = (
    ('Categories', '/' + CATEGORIES_SAVE_AS),
    ('Archive', '/' + ARCHIVES_SAVE_AS),
)

DISPLAY_CATEGORIES_ON_MENU = False
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.tables': {}
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ["plugins", "./pelican-plugins"]
PLUGINS = ["just_table"]

