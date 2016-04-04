#coding:utf8

from django.conf.urls import include, url,patterns
from django.contrib import admin
from hostinfo.views import index

admin.autodiscover()   #就是import 每一个应用下的admin.py

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hostinfo/$', index),
]
