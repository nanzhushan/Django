#coding:utf8

from django.shortcuts import render
from django.template.loader import render_to_string
import os

#上下文渲染器


# Create your views here.

#返回字典在模板中使用,(常规方式)

def home(request):
    return render(request, 'home.html', {'info': 'Welcome to knight !'})

def index(reuqest):
    return render(reuqest, 'index.html')


def columns(request):
    return render(request, 'columns.html')