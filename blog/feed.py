# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from blog.models import Entry

class LatestEntriesFeed(Feed):
    title = "catntent news"
    link = "/blog/feed/"
    description = "Neuigkeiten von catntent"

    def items(self):
        return Entry.public.order_by('-added')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
