from django.conf.urls import patterns, include, url
from django.conf import settings
from os import environ

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

debug = not environ.get("APP_NAME", "")

urlpatterns = patterns(
    '',
    url(r'^$', 'rrrp.views.index'),
    url(r'^', include('rrrp.urls')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #                        {'document_root': settings.STATIC_ROOT}),
)
if debug:
    urlpatterns += patterns('', url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),)