# -*- coding: utf-8 -*-
from django.db import models


class PubManager(models.Manager):
    """
    only return entries which are published.
    
    Depends on a boolean field named `published` on the model
    it is associated with.
    """
    def get_query_set(self):
        return super(PubManager, self).get_query_set().filter(published=True)
