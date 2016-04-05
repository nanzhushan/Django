#coding:utf8
from django.http import HttpResponse
from django.shortcuts import render

from os1 import lujin


def hello(request):
	return HttpResponse("这是hello的首页")




def hello1(request):
	context = {'name':'knight','age':'28'}
	aa = ['xx','yy','zz']
	bb = u"this is string"
	cc = 7
	dd = 99
	# return HttpResponse(aa[0])
	return HttpResponse(lujin)         #定义引入的模块
	# return render(request,'hello1.html',{'xxx':dd,'yyy':cc})     # 渲染必须是字典形式
