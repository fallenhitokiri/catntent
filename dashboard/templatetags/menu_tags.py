# -*- coding: utf-8 -*-
from django import template
from navigation.models import NavItem


register = template.Library()


@register.inclusion_tag('tags/navigation/navigation.html')
def navigation():
    items = NavItem.objects.all()
    return {'items': items}
