#coding:utf8

from django.conf.urls import include, url
from django.contrib import admin
from deploy.views import *

from asset.views import host_list,detail,create_host,delete_host,hindex,checkbox

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ttt/$',ttt,name="ttt"),
#    url(r'^deploy/remote_execution/$', remote_execution, name='remote_execution'),  # 执行远程命令
    url(r'^exe/$',exe_test),    ##原始的
    # url(r'^asset/host_list/$', host_list, name='host_list'),
    # url(r'^(?P<id>[0-9]+)/list/$', host_list, name='host_list'),
    url(r'^list/$', host_list, name='host_list'),
    # url(r'^list/(?P<id>[0-9]+)/$', detail, name='detail'),  ##传入id值
    url(r'^list/(?P<id>\d+)/$', detail, name='detail'),  ##传入id值,这是写法二

    url(r'^creat_host/$',create_host),      #添加新主机按钮
    # url(r'^delete_host/(?P<id>[0-9]+)/$', delete_host),  # 主机记录删除按钮
    # url(r'^delete_host/(?P<id>\d+)/$', delete_host),  # 主机记录删除,添加批量删除按钮，这是写法二
    url(r'^delete_host/(?P<id>[\d,]+)/$', delete_host),    ##匹配以逗号分开的数字多个以上,增加批量删除按钮

    url(r'^hindex/$', hindex),
    url(r'^checkbox/$',checkbox)

]
