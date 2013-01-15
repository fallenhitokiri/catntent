# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from utils.markup import markup


class SocialMedia(models.Model):
    SERVICE = (
            ('T', 'Twitter'),
            ('F', 'Facebook'),
            ('B', 'Blog'),
        )
    service = models.CharField(max_length=1, choices=SERVICE)
    username = models.CharField(max_length=200)

    def __unicode__(self):
        return self.username


class Profile(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    user = models.ForeignKey(User, related_name='profile', blank=True, null=True)
    picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    short = models.CharField(max_length=4000, blank=True)
    about_raw = models.TextField(blank=True)
    about = models.TextField(blank=True)
    social = models.ManyToManyField(SocialMedia, related_name='profile', blank=True, null=True)

    def __unicode__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        self.about = markup(self.about_raw)
        super(Profile, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        details = {
            'id': self.id,
            'last_name': self.last_name,
            'first_name': self.first_name,
        }
        return ('profiles:profile', (), details)
