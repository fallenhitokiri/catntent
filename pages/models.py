# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_delete

from managers.published import PubManager
from navigation.signals import update_navigation, delete_navigation
from utils.markup import markup


class Page(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    description = models.CharField(max_length=2000, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    content_raw = models.TextField()
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, blank=True, null=True)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")
    hidden = models.BooleanField(default=False)
    objects = models.Manager()
    public = PubManager()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.content = markup(self.content_raw)
        super(Page, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        details = {
            'id': self.id,
            'slug': self.slug
        }
        return ('pages:page', (), details)


post_save.connect(update_navigation, sender=Page)
pre_delete.connect(delete_navigation, sender=Page)
