#coding:utf-8

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404,render
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger   #导入分页器
from django.template import RequestContext,loader,Context

from ff.models import BlogsPost

# Create your views here.
"""
验证代码:
 f = open('d:\\ff.txt', 'w')
        f.write(query1)
        f.close()

"""

#模板页通过get方式提交数据,后台获取值
def fy(request):
    pnum = 1  #页数初始值

    posts = BlogsPost.objects.all()
    post1 = posts[0:2]   #提取前两个数据
    post2 = posts[2:4]

    postn = posts[(pnum-1)*2:pnum*2]    ##2 表示一页包含的内容

    query = request.GET.get('q', '')   #就是pagetype类型
    query1 = str(query)


    if query1 == "down":
        pnum += 1
        return render_to_response('1.html', {'list': post2})

    return render_to_response('1.html',{'list':postn})

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










