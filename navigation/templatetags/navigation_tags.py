# -*- coding: utf-8 -*-
from django import template
from navigation.models import Navigation


register = template.Library()


@register.inclusion_tag('tags/navigation/main-navigation.html')
def navigation(name):
    navigation = Navigation.objects.get(name=name)
    items = navigation.items.all()
    return {'items': items}
