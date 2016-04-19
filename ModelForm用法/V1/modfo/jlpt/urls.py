#coding:utf8

from django.conf.urls import include, url,patterns

urlpatterns = patterns('',
    url(r'^$', 'jlpt.views.home', name='home'),
)