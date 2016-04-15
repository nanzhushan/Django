#coding:utf8

from django.conf.urls import include, url
from django.contrib import admin
from uat.views import svnuat,jia,add,Mail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^svnuat/', svnuat),
    url(r'^jia/',jia),
    url(r'^add/',add),
    url(r'^mail',Mail)

]
