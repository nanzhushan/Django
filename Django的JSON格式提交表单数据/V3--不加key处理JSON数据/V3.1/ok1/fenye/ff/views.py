#coding:utf-8

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404,render
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger   #导入分页器
from django.template import RequestContext,loader,Context

from ff.models import BlogsPost
import simplejson
import json
from json import loads, dumps




# Create your views here.

##确实执行了post的方法

def json(request):
    if request.method == 'POST':
        data = loads((request.body).decode())    #获取json对象
        d1 = str(data)          #转换成str格式
        # d2 = eval(d1)

        f = open("d:\\knight.txt", 'w+')
        f.write(d1)
        f.close()


    return render_to_response('json.html')



###定义纯粹表单

def bd(request):
    if request.method == 'POST':
        name = request.POST.get('name');

        sex = request.POST['sex']
        return render_to_response('bd.html',{'name':name,'sex':sex})
        # return HttpResponse(u'你已经post提交了....')
    return render_to_response('bd.html')










