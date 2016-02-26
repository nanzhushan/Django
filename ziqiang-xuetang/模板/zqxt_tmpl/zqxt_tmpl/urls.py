#coding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views


urlpatterns = [
    url(r'^$', learn_views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
