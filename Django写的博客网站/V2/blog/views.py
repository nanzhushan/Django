#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#coding=utf-8
from django.shortcuts import render
from blog.models import BlogsPost
from django.shortcuts import render_to_response

# Create your views here.
#render_to_response()返回一个页面(index.html)，顺带把数据库中查询出来的所有博客内容（blog_list）也一并返回
def index(request):
    blog_list = BlogsPost.objects.all()
    hh = {"hello":"hello-----hello888"}
    yy = {"ho":"00000000000000"}
    return render_to_response('test.html',yy)       #render和render_to_response 传值都可以
    # return render(request,'test.html',hh)            #必须是字典形式
    # return HttpResponse(u"欢迎光临 自强学堂!")
    # return render(request,'test.html')

    # return render_to_response('index.html',{'blog_list':blog_list})   #渲染字典形式

