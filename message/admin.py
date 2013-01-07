# -*- coding: utf-8 -*-
from django.contrib import admin
from message.models import Message


class DefaultAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'added', 'done')


admin.site.register(Message, DefaultAdmin)
