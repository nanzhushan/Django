#coding:utf8
# 定义路由
import blog
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import *
from blog.views import archive                 #导入函数和方法
from blog.views import add,index,indexp

urlpatterns = {
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', archive),        #执行archive的函数
    # url(r'^$', index),
    url(r'^index/$', index),  #执行index的函数,post提交
    url(r'^indexp/$',indexp),
    url(r'^add/$', add),  ##url 执行blog.views下的add的函数
}

