#coding:utf-8
from django.contrib import admin
from hostinfo.models import Host

# Register your models here.

#注册后台admin并显示注册信息
class HostAdmin(admin.ModelAdmin):
    list_display = [
        'hostname',
        'ip',
        'osversion',
        'memory',
        'disk',
        'vendor_id',
        'model_name',
        'cpu_core',
        'product',
        'Manufacturer',
        'sn']


admin.site.register(Host,HostAdmin)