# coding:utf-8
#from django.http import HttpResponse
#控制层
from django.shortcuts import render

def hello(request):
    context = {}
    #
    context['hello'] = 'Hello World !第二次修改'
 
    #return render(request, 'hello.html', context)
 #   return render(request, 'cc.html', context)   #测试新加的html页面
    return render(request, 'a.js', context)   #测试新加的html页面
   