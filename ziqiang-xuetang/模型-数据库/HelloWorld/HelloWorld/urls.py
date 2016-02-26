#coding:utf-8
#控制层contronl 的配置文件
from django.conf.urls import *
from HelloWorld.view import hello

urlpatterns = patterns("",
    ('^hello/$', hello),
)