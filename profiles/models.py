# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from common.utils.markup import markup
from utils import normalize_username


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

    def save(self, *args, **kwargs):
        self.username = normalize_username(self.service, self.username)
        super(SocialMedia, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        if self.service == 'T':
            return "https://www.twitter.com/{0}".format(self.username)
        if self.service == 'F':
            return "https://www.facebook.com/{0}".format(self.username)
        if self.service == 'B':
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
