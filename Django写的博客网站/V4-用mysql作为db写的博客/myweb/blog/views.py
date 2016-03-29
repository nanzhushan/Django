#coding:utf8
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogsPost


from django.shortcuts import render_to_response

# Create your views here.
def archive(request):
    posts = BlogsPost.objects.all()    #获取数据库里面所拥有BlogsPost对象
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})
    # return HttpResponse("这是博客首页")
    return HttpResponse(t.render(c))        #渲染到archive.html上