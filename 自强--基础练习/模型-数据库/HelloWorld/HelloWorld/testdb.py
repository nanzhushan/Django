#coding:utf-8
from django.conf.urls import  *
from HelloWorld.view import hello
from HelloWorld.testdb import testdb


urlpatterns = patterns("",
                       ('^hello/$',hello),
                       ('^testdb/$',testdb),
                       
                       )

