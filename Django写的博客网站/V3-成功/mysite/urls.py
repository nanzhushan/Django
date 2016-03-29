#coding:utf8
# 定义路由

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import *
from blog.views import archive                 #导入函数和方法

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', archive),
]

