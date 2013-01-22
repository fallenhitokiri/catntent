# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType


class NavItem(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    order = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=200, blank=True)
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name


class Navigation(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    items = models.ManyToManyField(NavItem, blank=True, null=True)

    def __unicode__(self):
        return self.name
