# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Entry, Article, Note, Link, Picture, Tag, Category, ImageAttachment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'added', 'changed', 'user', 'published')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class AttachmentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class EntryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'added', 'user', 'published')


class InfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, PostAdmin)
admin.site.register(Note, PostAdmin)
admin.site.register(Link, PostAdmin)
admin.site.register(Picture, PostAdmin)

admin.site.register(ImageAttachment, AttachmentAdmin)

admin.site.register(Entry, EntryAdmin)

admin.site.register(Tag, InfoAdmin)
admin.site.register(Category, InfoAdmin)
