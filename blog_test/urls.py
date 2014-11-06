# -*- coding: utf8 -*-
from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = patterns('',
    # frontend
    url(r'^', include('blog.urls', namespace='blog')),

    # backend
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
)

# Необходимо для доступа к media в DEBUG-режиме
if settings.DEBUG:
    #import debug_toolbar
    urlpatterns = patterns('',
        url(
            r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
        #url(r'^__debug__/', include(debug_toolbar.urls)),
    ) + staticfiles_urlpatterns() + urlpatterns