# -*- coding: utf-8 -*-
from django.contrib import admin
from profiles.models import SocialMedia, Profile


class SocialMediaAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Profile, ProfileAdmin)
