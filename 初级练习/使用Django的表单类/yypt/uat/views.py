#coding:utf8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse
import os

#引入表单类
from .form import MailForm
# Create your views here.

def svnuat(request):
    query = request.GET.get('q','') #request.GET是一个类字典对象，它包含所有GET请求的参数，这里表示取得name为'q'的参数值
    query1 = str(query)
    if query1 == "update":      # 判断get方式提交的值
        results = '你使用 %s，更新了uat的svn节点' % query1
        f = open('c:\\11111.txt','w')      # 执行shell命令
        f.close()

    elif query1 == "update-restart":
        results = '你使用 %s，更新了uat的svn节点,并重启了该节点应用' % query1
        f = open('c:\\restart.txt', 'w')  # 执行shell命令
        f.close()

    else:
      results = ['it has failed....']

    return render_to_response('svnuat.html', {'results': results})


def jia(request):
    return render(request, 'jia.html')

def add(request):
    # return HttpResponse("this is add")
    a = request.GET['a']
    b = request.GET['b']
    # return HttpResponse(b)
    a = int(a)
    b = int(b)

    return HttpResponse(a+b)



##使用引入的表单类并渲染到模板
def Mail(request):
    if request.method == 'POST':  # 当提交表单时
        form = MailForm(request.POST)  # form 包含提交的数据

        # if form.is_valid():  # 如果提交的数据合法
        #     username = form.cleaned_data['username']
        #     email = form.cleaned_data['email']
        #     return HttpResponse(u"提交的数据合法")

    else:  # 当正常访问时
        form = MailForm()   ##实例化表单，取表单内容

    return render(request,'mail.html',{'form':form})

