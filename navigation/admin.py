# -*- coding: utf-8 -*-
from django.contrib import admin
from navigation.models import NavItem, Navigation


class DefaultAdmin(admin.ModelAdmin):
    pass


class NavItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'url')


admin.site.register(Navigation, DefaultAdmin)
admin.site.register(NavItem, NavItemAdmin)
