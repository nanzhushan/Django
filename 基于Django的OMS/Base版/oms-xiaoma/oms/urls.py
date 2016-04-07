#coding:utf8

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# 导入各个app的视图
from asset.views import *
from oms.views import index
from installed.views import system_install_managed,system_install_list,system_install,system_install_record
from deploy.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^oms/admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),

    ##asset的app下的方法，从数据库里查数据以及删数据然后渲染到页面
    url(r'^asset/host_list/$', host_list, name='host_list'),
    url(r'^asset/add_host/$', host_list_manage, name='add_host'),   # 定义添加主机页面,从asset的app里导入
    url(r'^asset/delete_host/$', host_list_manage, name='host_delete'),
    url(r'^asset/host_manage/(?P<id>\d+)/$', host_list_manage, name='host_manage'),
    url(r'^asset/server_asset/$', server_asset_list, name='server_asset_list'),
    url(r'^asset/server_get/$', get_server_asset, name='get_server_asset'),
    url(r'^asset/device_list/$', network_device_list, name='network_device_list'),      #定义网络设备列表页面
    url(r'^asset/device_add/$', network_device_discovery, name='add_device'),
    url(r'^asset/idc_list/$', idc_asset_list, name='idc_asset_list'),
    url(r'^asset/add_idc/$', idc_asset_manage, name='add_idc'),

                       ###install的app下的view定义的方法
    url(r'^install/install_list/$', system_install_list, name='install_list'),
    url(r'^install/install_manage/(?P<id>\d+)/$', system_install_managed, name='install_manage'),
    url(r'^install/system_install/$',system_install, name='system_install'),
    url(r'^install/install_record/$',system_install_record, name='install_record'),
                    ###deploy的app下的view定义的方法
    url(r'^deploy/key_list/$', salt_key_list, name='key_list'),
    url(r'^deploy/key_delete/$', salt_delete_key, name='delete_key'),
    url(r'^deploy/key_accept/$', salt_accept_key, name='accept_key'),
    url(r'^deploy/module_deploy/$', module_deploy, name='module_deploy'),
    url(r'^deploy/remote_execution/$', remote_execution, name='remote_execution'),
    url(r'^deploy/code_deploy/$', code_deploy, name='code_deploy'),
)
