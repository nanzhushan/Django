#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin
from xx_tab.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'add/$', xx_tab_add),
    # url(r'list/$', views.get_xx_tabs, ),
    # url(r'detail/([0-9]+)$', views.get_xx_tab),
    # url(r'delete/([0-9]+)$', views.delete_xx_tab),
    # url(r'update/([0-9]+)$', views.update_xx_tab),


]
