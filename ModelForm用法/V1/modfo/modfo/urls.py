#coding:utf8

from django.conf.urls import include, url
from django.contrib import admin

# 使用include的函数
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^jlpt/',include('jlpt.urls')),
]
