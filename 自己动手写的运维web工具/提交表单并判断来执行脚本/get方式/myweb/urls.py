#coding:utf8
# 定义路由
import blog
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import *

from blog.views import test

urlpatterns = {
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', archive),
    
    url(r'^test/', test),
}

