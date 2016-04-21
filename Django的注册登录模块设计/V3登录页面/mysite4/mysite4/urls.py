#coding:utf8

from django.conf.urls import include, url,patterns
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls')),
]
