#coding:utf8

from django.conf.urls import include, url
from django.contrib import admin
from lesson.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^book/(\d+)',book_list)
]
