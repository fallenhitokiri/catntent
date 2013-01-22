# -*- coding: utf-8 -*-
from django.contrib import admin
from pages.models import Page, Image


class DefaultAdmin(admin.ModelAdmin):
    pass


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'changed', 'user', 'published')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Image, DefaultAdmin)

admin.site.register(Page, PageAdmin)
