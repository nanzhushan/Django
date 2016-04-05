#coding:utf8
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Xx_Tab

# Create your views here.

#定义 路由中转向的 add_xx_tab函数

##装饰器
@api_view(['POST', 'GET'])
def xx_tab_add(request, *args):
    if request.method == 'GET':
        return HttpResponse("这是get方法")
    elif request.method == 'POST':
        return HttpResponse("this is post")


