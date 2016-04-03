#coding:utf8
from django.conf import settings as original_settings

##新建两个上下文渲染器，要在settings.py 添加

def settings(request):
    return {'settings': original_settings}

def ip_address(request):
    return {'ip_address': request.META['REMOTE_ADDR']}