#coding:utf8
from django.conf.urls import patterns, url
from online import views


urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),              #登录页
    url(r'^login/$',views.login,name = 'login'),        #登录页
    url(r'^regist/$',views.regist,name = 'regist'),      #注册页
    url(r'^index/$',views.index,name = 'index'),            #登录成功页面
    url(r'^logout/$',views.logout,name = 'logout'),             #注销
    url(r'^list/$',views.list,name='list'),                             #list页面来验证是不是需要登录才能进行访问
    url(r'^list2/$', views.list2, name='list2'),
)