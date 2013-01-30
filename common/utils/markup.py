# -*- coding: utf-8 -*-
from django.conf import settings


def _markdown(text):
    from markdown2 import markdown
    return markdown(text)


def markup(text):
    """convert text to html"""
    if settings.MARKUP == "markdown":
        return _markdown(text)
    if settings.MARKUP == "none":
        return text
