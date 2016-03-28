#coding:utf8
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import BlogsPost
from django.shortcuts import render_to_response
from blog.ttt1 import *


# Create your views here.

def index(request):

    context = {'hello':'Hello World!dddd7778',"name":"knight"}
    #sql2 = {'id':dd1.fetchall()}

    sql3 = {'id3':id3}
    blog_list = BlogsPost.objects.all()
    # return blog_list       #too many values to unpack 表示太多的值
    #  return HttpResponse(u"hello..fff000..")
    # return render_to_response('index.html',{'blog_list':blog_list})    ##渲染
    # return render_to_response('test.html',{'blog_list':blog_list})
    # return render_to_response('test.html')      #不传值
    return  render(request,'test.html',sql3)