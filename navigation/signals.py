# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType

from navigation.models import NavItem


def in_navigation(instance):
    """check conditions for page to get a navitem"""
    return (instance.published == True) and \
           (instance.hidden == False)


def delete_navitem(instance):
    """delete navitem if it exists"""
    try:
        ctype = ContentType.objects.get_for_model(instance)
        navitem = NavItem.objects.get(content_type=ctype, object_id=instance.id)
        navitem.delete()
    except NavItem.DoesNotExist:
        pass


def update_navigation(sender, **kwargs):
    """create / change NavItem (navigation) when a page is edited"""
    if 'created' in kwargs:
        instance = kwargs['instance']
        if in_navigation(instance):
            ctype = ContentType.objects.get_for_model(instance)
            navitem = NavItem.objects.get_or_create(content_type=ctype, object_id=instance.id)[0]
            navitem.name = instance.name
            navitem.url = instance.get_absolute_url()

            if instance.parent == None:
                navitem.mainnav = True

            navitem.save()
        else:
            delete_navitem(instance)


def delete_navigation(sender, **kwargs):
    """delete navigation item if is deleted"""
    delete_navitem(kwargs['instance'])
