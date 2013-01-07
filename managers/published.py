# -*- coding: utf-8 -*-
from django.db import models


class PubManager(models.Manager):
    """only return entries which are published"""
    def get_query_set(self):
        return super(PubManager, self).get_query_set().filter(published=True)
