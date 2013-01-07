from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^message/', include('message.urls', namespace="message")),
    url(r'^pages/', include('pages.urls', namespace="pages")),
    url(r'^portfolio/', include('portfolio.urls', namespace="portfolio")),

    url(r'^admin/', include(admin.site.urls)),
)
