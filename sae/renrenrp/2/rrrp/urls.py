from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    'rrrp.views',
    url(r'^index/$', 'index'),
    url(r'^login/$', 'login'),
    url(r'^fresh/$', 'fresh'),
    url(r'^clearLog/$', 'clearLog'),
    url(r'^user/(.+)/addUser$', 'addUser'),
    url(r'^user/(.+)/$', 'user', name='user'),
    url(r'^login/$', 'login'),
)
