#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import index

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'blog.views.index'),   ##也可以是直接index
)