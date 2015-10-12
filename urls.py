from django.conf.urls import patterns, include, url
from django.views.generic import FormView
from . import views

urlpatterns = patterns('',
    url(r'^(?P<config>[a-z0-9_-]{1,10})/$', views.listProject, name='views.listProject'),
    url(r'^(?P<project>[a-z0-9_-]{1,10})/(?P<config>[a-z0-9_-]{1,10})/$', views.viewConfigItem, name='views.viewConfigItem'), 
    url(r'^(?P<project>[a-z0-9_-]{1,10})/(?P<config>[a-z0-9_-]{1,10})/edit/$', views.doConfigItem, name='views.doConfigItem'), 
    url(r'^(?P<project>[a-z0-9_-]{1,10})/(?P<config>[a-z0-9_-]{1,10})/export/$', views.exportConfigItem, name='views.exportConfigItem'),
)
