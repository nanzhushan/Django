#coding:utf-8

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404,render
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger   #导入分页器
from django.template import RequestContext,loader,Context

from ff.models import BlogsPost

# Create your views here.

def json(request):
    if request.method == 'POST':
        return HttpResponse(u'你已经通过json格式post了数据')
    # return HttpResponse(u"这是json测试页面....")
    return render_to_response('json.html')



def bd(request):
    if request.method == 'POST':
        name = request.POST.get('name');

        sex = request.POST['sex']
        return render_to_response('bd.html',{'name':name,'sex':sex})
        # return HttpResponse(u'你已经post提交了....')
    return render_to_response('bd.html')










