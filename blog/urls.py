# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from blog.feed import LatestEntriesFeed


urlpatterns = patterns('blog',
    url(r'^$', 'views.home', name="home"),
    url(r'^archive/$', 'views.archive', name="archive"),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)$', 'views.entry', name="entry"),
    url(r'^feed/$', LatestEntriesFeed(), name="feed"),
)
