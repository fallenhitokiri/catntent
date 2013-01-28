# -*- coding: utf-8 -*-
from django import template
from blog.models import Category, Tag


register = template.Library()


@register.inclusion_tag('blog/template-tags/categories.html')
def categories():
    categories = Category.objects.all()
    return {'categories': categories}


@register.inclusion_tag('blog/template-tags/tags.html')
def tags():
    tags = Tag.objects.all()
    return {'tags': tags}
