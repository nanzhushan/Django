#coding:utf8

from django.conf.urls import include, url
from django.contrib import admin
import blog.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$',blog.views.home),
]
