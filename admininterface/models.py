# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify


class Module(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Module, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        path = 'admininterface.{0}'.format(self.slug)
        details = {
            'id': self.id,
            'slug': self.slug
        }
        return (path, (), details)
