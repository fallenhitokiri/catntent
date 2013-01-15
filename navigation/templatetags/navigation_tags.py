# -*- coding: utf-8 -*-
from django import template
from navigation.models import NavItem


register = template.Library()


@register.inclusion_tag('tags/navigation/main-navigation.html')
def mainnavigation():
    items = NavItem.main.all()
    return {'items': items}
