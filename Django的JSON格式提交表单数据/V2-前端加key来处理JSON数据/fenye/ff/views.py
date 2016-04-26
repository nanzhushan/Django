#coding:utf-8

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404,render
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger   #导入分页器
from django.template import RequestContext,loader,Context

from ff.models import BlogsPost
import simplejson
import json



# Create your views here.

##确实执行了post的方法
def json(request):
    if request.method == 'POST':
        jj = request.POST.get('haha')
        jj1 = str(jj)

        # req = simplejson.loads(request.raw_post_data)
        # # # name = request.POST.get('name')
        # li = "444"
        #
        f = open("d:\\4455.txt", 'w+')
        f.write(jj1)
        f.close()

        # req = simplejson.loads(request.raw_post_data)    ##request.raw_post_data 的原始数据转换成字典类型
        # return HttpResponse(req)
        # return render_to_response('json.html')
    # return HttpResponse(u"这是json测试页面....")

    return render_to_response('json.html')







def bd(request):
    if request.method == 'POST':
        name = request.POST.get('name');

        sex = request.POST['sex']
        return render_to_response('bd.html',{'name':name,'sex':sex})
        # return HttpResponse(u'你已经post提交了....')
    return render_to_response('bd.html')










