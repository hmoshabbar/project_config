from django.conf.urls import patterns, include, url
from django.views.generic import FormView
from . import views

urlpatterns = patterns('',
#     url(r'^$', upload, name='upload'),
#     url(r'^all', AllView.as_view(), name='all'), 
#     url(r'^(?P<path>.*)$', OneView.as_view(), name='one'), 
    url(r'^$', views.base, name='project_config.base'),
    url(r'^(?P<project>[a-z0-9_-]{1,10})/(?P<config>[a-z0-9_-]{1,10})/$', views.viewConfigItem, name='views.viewConfigItem'), 
    url(r'^(?P<project>[a-z0-9_-]{1,10})/(?P<config>[a-z0-9_-]{1,10})/edit/$', views.doConfigItem, name='views.doConfigItem'), 
    url(r'^(?P<project>[a-z0-9_-]{1,10})/(?P<config>[a-z0-9_-]{1,10})/export/$', views.exportConfigItem, name='views.exportConfigItem'),
    url(r'^(?P<project>[a-z0-9_-]{1,10})/(?P<config>[a-z0-9_-]{1,10})/plist/$', views.doPlist, name='views.doPlist'), 
    url(r'^(?P<project>[a-z0-9_-]{1,10})/(?P<config>[a-z0-9_-]{1,10})/plist/gen$', views.generatePlist, name='views.generatePlist'), 
)
