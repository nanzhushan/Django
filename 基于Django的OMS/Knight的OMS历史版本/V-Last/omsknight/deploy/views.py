#coding:utf8
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

import os
##
# from saltapi import *
#导入数据库model
from asset.models import HostList


##################################

# Create your views here.

def ttt(request):
    return HttpResponse(u'this is ttt....url')

@login_required
def exe_test(request):
    if not request.user.is_authenticated():
        return HttpResponse(u"请先登录...")

    if request.method == 'GET':
        return render_to_response("exe.html")
    # return HttpResponse("这是测试执行命令的")
    elif request.method == 'POST':
        danger = ('rm', 'reboot', 'init', 'shutdown')     ##定义危险命令
        ctx = {}
        ctx['a2'] = request.POST['a']
        a22 = request.POST['a']               #获取ip地址
        tgt = request.POST['a']
        anew = a22.split(',')     #切片变成列表

        tgtcheck = "true"      #先设置空值,后面的if会有赋值

        ctx['b2'] = request.POST['b']
        b22 = request.POST['b']
        b22check = b22 not in danger

        # tgtcheck = HostList.objects.filter(ip=a22)                #能查到值就为真，否则为假
        ##开始比较
        if a22 == "" or b22 == "":
            return HttpResponse(u"主机ip或者cmd.run命令不能为空值...")

        for i in anew:
            if not HostList.objects.filter(ip=i):    #可以查到记录
                tgtcheck = "error"                   #只要有一个不通过就是error
            else:
              pass




        # return HttpResponse(tgtcheck)
        if b22check and  tgtcheck == "true":
            return HttpResponse(u"目标主机存在，并且不是危险命令，可以执行远程命令的操作....")
        elif not b22check:
            return HttpResponse(u"你这是危险命令，无法执行下一步操作....")
        elif tgtcheck == "error":
            return  HttpResponse(u"目标主机不存在,请重新输入....")





