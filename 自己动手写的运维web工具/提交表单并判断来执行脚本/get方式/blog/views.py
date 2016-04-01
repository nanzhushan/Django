#coding:utf8
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogsPost
# from blog.models import StudentPost
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import os


def test(request):
    query = request.GET.get('q','') #request.GET是一个类字典对象，它包含所有GET请求的参数，这里表示取得name为'q'的参数值
    query1 = str(query)
    if query1 == "update":      # 判断get方式提交的值
        results = '你使用 %s，更新了uat的svn节点' % query1
        f = open('c:\\11111.txt','w')      # 执行shell命令
        f.close()

    else:
      results = ['it has failed....']

    return render_to_response('test.html', {'results': results})
	
    
