#coding:utf8
from django.conf.urls import include, url
from django.contrib import admin

from asset.views import *
from installed.views import *
from .views import *
from deploy.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),

    # url(r'^$', 'django.contrib.auth.views.login', name='login'),
    url(r'^account/', include('account.urls')),

    url(r'^asset/record$', record, name='record'),
    url(r'^asset/host_list/$', host_list, name='host_list'),
    url(r'^asset/add_host/$', host_list_manage, name='add_host'),
    url(r'^asset/host_manage/(?P<id>\d+)/$', host_list_manage, name='host_manage'),
    url(r'^asset/delete_host/$', host_list_manage, name='host_delete'),

    url(r'^install/install_list/$', system_install_list, name='install_list'),
    url(r'^install/install_manage/(?P<id>\d+)/$', system_install_managed, name='install_manage'),
    url(r'^install/install_manage/$', system_install_managed, name='system_manage'),
    url(r'^install/system_install/$',system_install, name='system_install'),
    url(r'^install/install_record/$',system_install_record, name='install_record'),

    url(r'^deploy/key_list/$', salt_key_list, name='key_list'),
    url(r'^deploy/key_delete/$', salt_delete_key, name='delete_key'),
    url(r'^deploy/key_accept/$', salt_accept_key, name='accept_key'),
    url(r'^deploy/module_deploy/$', module_deploy, name='module_deploy'),
    url(r'^deploy/remote_execution/$', remote_execution, name='remote_execution'),
    # url(r'^deploy_1/code_deploy/$', code_deploy, name='code_deploy'),
]
