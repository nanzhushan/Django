#coding:utf8

from django.conf.urls import include, url
from django.contrib import admin
from online.views import myview
urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^online/',include('online.urls')),
]
