# -*- coding: utf-8 -*-
from django.db import models


class MainNavigationManager(models.Manager):
    """only return entries which are published"""
    def get_query_set(self):
        return super(MainNavigationManager, self).get_query_set().filter(mainnav=True)