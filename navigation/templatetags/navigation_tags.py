# -*- coding: utf-8 -*-
from django import template
from navigation.models import Navigation


register = template.Library()


@register.inclusion_tag('navigation/template-tags/navigation.html')
def navigation(name):
    try:
        navigation = Navigation.objects.get(name=name)
        items = navigation.items.all()
        return {'items': items}
    except:
        return None
