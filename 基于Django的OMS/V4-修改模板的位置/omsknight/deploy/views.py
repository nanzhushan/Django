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


def exe_test(request):
    if request.method == 'GET':
        return render_to_response("gp1.html")
    # return HttpResponse("这是测试执行命令的")
    elif request.method == 'POST':
        danger = ('rm', 'reboot', 'init', 'shutdown')     ##定义危险命令
        ctx = {}
        ctx['a2'] = request.POST['a']
        a22 = request.POST['a']               #赋值
        tgt = request.POST['a']               #赋值

        a3 = request.POST['a']
        ctx['b2'] = request.POST['b']
        b22 = request.POST['b']
        b22check = b22 not in danger

        tgtcheck = HostList.objects.filter(hostname=a22)    #能查到值就为真，否则为假
        # return HttpResponse(tgtcheck)
        if b22check and tgtcheck:
            return HttpResponse(u"目标主机存在，并且不是危险命令，执行远程命令的操作....")
        elif not b22check:
            return HttpResponse(u"你这是危险命令，无法执行下一步操作....")
        elif not tgtcheck:
            return  HttpResponse(u"目标主机不存在,请重新输入....")




        # if not b22check:                                        #判断是不是危险命令
        #     return HttpResponse(u"你这是危险命令，无法操作.............")
        # else:
        #     return HttpResponse(u"第二个文本框的输入值是:"+b22)



