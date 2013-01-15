# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('profiles',
    url(r'^$', 'views.home', name="home"),
    url(r'^(?P<id>\d+)-(?P<last_name>[-\w]+)-(?P<first_name>[-\w]+)$', 'views.detail', name="detail"),
)
