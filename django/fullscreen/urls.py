from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'fullscreen.apps.events.views.home', name='home'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^(?P<path>(css|fonts|images|js|media)/.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )