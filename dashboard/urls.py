# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('dashboard',
    url(r'^$', 'views.home', name="home")
)
