#coding:utf-8

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404,render
# from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger   #不用分页器
from django.template import RequestContext,loader,Context

from ff.models import BlogsPost

# Create your views here.
#模板页通过get方式提交数据,后台获取值,要注意前台href也有变量

def fy(request):
    page = request.GET.get('page','')    #获取key对应的值,也就是page后的变量
    ##try发生异常就执行except语句

    try:
        page_num = int(page)
    except:
        page_num = 0
    if page_num == 0:
        pre_page = 0
        next_page = 1
    else:
        pre_page = page_num - 1
        next_page = page_num + 1

    posts = BlogsPost.objects.all()
    postn = posts[page_num * 2:(page_num+1) * 2]

    return render_to_response('1.html', {'list': postn,'next_page':next_page,'pre_page':pre_page})









