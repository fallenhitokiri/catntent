# -*- coding: utf-8 -*-
from operator import attrgetter
from itertools import chain

from django.core.paginator import Paginator


def paginate(entries, current_page=False, count=5):
    """return paginated list and paginator for entries"""
    paginator = Paginator(entries, count)

    if not current_page:
        current_page = 1

    try:
        return paginator.page(current_page)
    except:
        return paginator.page(paginator.num_pages)


def merge_query_sets(articles, notes, links, pictures):
    """
    suboptimal helper method to work around some limitations with
    generic relations and the way M2M fields are saved

    used for Tags and Categories
    """
    entries = []

    for item in list(chain(articles, notes, links, pictures)):
        if item.published is True:
            entries.append(item.entry.all()[0])

    entries = sorted(entries, key=attrgetter('added'))
    return entries
