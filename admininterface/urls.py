# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('admininterface',
    url(r'^$', 'views.home', name="home"),
    #url(r'^archive/$', 'views.archive', name="archive"),
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)$', 'views.entry', name="entry"),
    #url(r'^feed/$', LatestEntriesFeed(), name="feed"),
)
