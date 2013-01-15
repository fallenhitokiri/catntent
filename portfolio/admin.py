from django.contrib import admin
from portfolio.models import Tech, Job, Shot, Testimonial, Customer, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'added', 'user', 'published')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class DefaultAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tech, DefaultAdmin)
admin.site.register(Job, DefaultAdmin)
admin.site.register(Shot, DefaultAdmin)
admin.site.register(Testimonial, DefaultAdmin)
admin.site.register(Customer, DefaultAdmin)

admin.site.register(Project, ProjectAdmin)
