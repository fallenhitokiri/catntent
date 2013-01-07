# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('message',
    url(r'^$', 'views.home', name="home"),
)
