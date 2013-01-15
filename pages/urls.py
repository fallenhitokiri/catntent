# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('pages',
    url(r'^(?P<id>\d+)-(?P<slug>[-\w]+)$', 'views.page', name="page"),
)
