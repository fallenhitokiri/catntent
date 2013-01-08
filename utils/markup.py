# -*- coding: utf-8 -*-

def markdown(text):
    from markdown2 import markdown
    return markdown(text)


def markup(text):
    """convert text to html"""
    return markdown(text)
