from django.contrib import admin
from portfolio.models import Tech, Job, Shot, Project


class DefaultAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tech, DefaultAdmin)
admin.site.register(Job, DefaultAdmin)
admin.site.register(Shot, DefaultAdmin)
admin.site.register(Project, DefaultAdmin)
