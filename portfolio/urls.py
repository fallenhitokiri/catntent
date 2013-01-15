from django.conf.urls import patterns, url


urlpatterns = patterns('portfolio',
    url(r'^$', 'views.home', name="home"),
    url(r'^(?P<id>\d+)-(?P<slug>[-\w]+)$', 'views.project', name="project"),
)
