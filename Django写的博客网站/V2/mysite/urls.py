#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
# from blog import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'blog.views.index'),            #执行blog.view.下的index类
)