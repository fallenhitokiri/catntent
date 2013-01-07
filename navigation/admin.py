# -*- coding: utf-8 -*-
from django.contrib import admin
from navigation.models import NavItem


class DefaultAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'url')

admin.site.register(NavItem, DefaultAdmin)
