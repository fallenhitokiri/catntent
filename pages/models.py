# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_delete
from django.contrib.contenttypes.models import ContentType

from managers.published import PubManager
from navigation.models import NavItem
from utils.markup import markup


class Page(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
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


def in_navigation(instance):
    """check conditions for page to get a navitem"""
    return (instance.parent == None) and \
           (instance.published == True) and \
           (instance.hidden == False)


def delete_navitem(instance):
    """delete navitem if it exists"""
    try:
        ctype = ContentType.objects.get_for_model(instance)
        navitem = NavItem.objects.get(content_type=ctype,
                                      object_id=instance.id)
        navitem.delete()
    except NavItem.DoesNotExist:
        pass


def update_navigation(sender, **kwargs):
    """create / change NavItem (navigation) when a page is edited"""
    if 'created' in kwargs:
        instance = kwargs['instance']
        if in_navigation(instance):
            ctype = ContentType.objects.get_for_model(instance)
            navitem = NavItem.objects.get_or_create(content_type=ctype,
                                                    object_id=instance.id)[0]
            navitem.name = instance.name
            navitem.url = instance.get_absolute_url()
            navitem.save()
        else:
            delete_navitem(instance)


def delete_navigation(sender, **kwargs):
    """delete navigation item if is deleted"""
    delete_navitem(kwargs['instance'])


post_save.connect(update_navigation, sender=Page)
pre_delete.connect(delete_navigation, sender=Page)
