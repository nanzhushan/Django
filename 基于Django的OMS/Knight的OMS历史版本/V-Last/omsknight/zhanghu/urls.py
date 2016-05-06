#coding:utf8
from django.conf.urls import patterns, url
from zhanghu import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),              #登录页
    url(r'^login/$',views.login,name = 'login'),        #登录页
    url(r'^logout/$',views.logout,name = 'logout'),             #注销
    url(r'^success/$', views.success),
    url(r'^list3/$', views.list3, name='list3'),              ##使用装饰器
)