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
        d4 = loads((request.body).decode())    #获取json对象
        d1 = str(d4)          #转换成str格式
        data = eval(d1)             #转换成字典
        data.update(name='knight', sex='man')      #获取的json数据进行处理

        f = open("d:\\ttt.txt",'w+')    #写入文件对传过来的json数据进行处理
        f.write(data['name'])
        f.close()

        dh = '{"name":"xixi","sex":"haha"}'              ##字符串形式,回调函数必须取字符串,最外面必须是单引号，里面是双引号
        return HttpResponse(dh)

    return render_to_response('json.html')












