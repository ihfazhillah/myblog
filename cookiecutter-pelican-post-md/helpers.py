"""Membuat jinja ext for slugify"""
import datetime
from slugify import slugify
from jinja2.ext import Extension


class SlugifyExtension(Extension):
    """Jinja2 extension to convert a string to slug"""

    def __init__(self, environment):
        super(SlugifyExtension, self).__init__(environment)
        environment.filters['slugify'] = slugify


class NowExtension(Extension):
    """Jinja2 extension to add extra now context"""

    def __init__(self, environment):
        super(NowExtension, self).__init__(environment)
        environment.globals['now'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
