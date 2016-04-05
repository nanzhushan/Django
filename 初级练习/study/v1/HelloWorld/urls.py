#coding:utf8
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import *
from HelloWorld.view import hello
from HelloWorld.view import hello1       #导入模块的方法

urlpatterns = patterns("",
	('^hello/$', hello),
    ('^hello1/$',hello1),     #执行hello1的函数
)