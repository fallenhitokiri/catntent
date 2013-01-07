# -*- coding: utf-8 -*-
from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=400)
    added = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False, blank=True)
    mail = models.EmailField()
    message = models.TextField()

    class Meta:
        ordering = ['-added']

    def __unicode__(self):
        return "[{0}] {1}".format(self.added, self.name)
