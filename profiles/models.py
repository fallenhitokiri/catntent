# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class SocialMedia(models.Model):
    SERVICE = (
            ('T', 'Twitter'),
            ('F', 'Facebook'),
            ('B', 'Blog'),
        )
    service = models.CharField(max_length=1, choices=SERVICE)
    url = models.URLField(verify_exists=True)

    def __unicode__(self):
        return "{0} {1} - {2}".format(self.profile.user.first_name, self.profile.user.last_name, self.service)


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile')
    picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    short = models.CharField(max_length=4000, blank=True)
    about_raw = models.TextField(blank=True)
    about = models.TextField(blank=True)
    social = models.ManyToManyField(SocialMedia, related_name='profile', blank=True, null=True)

    def __unicode__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

    def get_absolute_url(self):
        details = {
            'user': self.user.id,
            'last_name': self.user.last_name,
            'first_name': self.user.first_name,
        }
        return ('profiles:user', (), details)
