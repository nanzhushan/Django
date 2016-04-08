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
from saltapi import *

##################################

# Create your views here.

def ttt(request):
    return HttpResponse(u'this is ttt....url')


def exe_test(request):
    if request.method == 'GET':
        return render_to_response("get_post.html")
    # return HttpResponse("这是测试执行命令的")
    elif request.method == 'POST':
        ctx = {}
      #  ctx['a1'] = int(request.POST['a'])  # 字典里插入data
        ctx['a2'] = request.POST['a']
        a22 = request.POST['a']               #赋值
        tgt = request.POST['a']               #赋值

        a3 = request.POST['a']
     #   ctx['b1'] = int(request.POST['b'])  # post提交的是str类型，所以要转换,用int转换
        ctx['b2'] = request.POST['b']
        b22 = request.POST['b']               #赋值
        arg = request.POST['b']               #赋值

#       ctx['c1'] = ctx['a1'] + ctx['b1']
#	a3r = a3+" :this is a"
	#os.system("salt 'ctx[a2]' cmd.run 'touch ccc'")
#	os.system("touch /root/331.txt")          ##执行系统的shell命令
#	os.environ['a22']=str(a22)
#	os.environ['b22']=str(b22)
#	os.system('salt $a22 cmd.run "$b22"')	  ##python的变量传到shell中

       # f = open('/root/33.txt',"w+")             #写入文件清除原有的内容，再写入，如果是追加用"a+"
       # f.writelines(ctx['a2'])
        #return HttpResponse(a3r)
        #return HttpResponse("执行成功")
	sapi = saltAPI()                          ##实例化类
#	params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg}

#	params = {'client':'local','tgt':tgt, 'fun':'cmd.run', 'arg':arg}	#这种方式也可以访问，下面也行，只是下面已经是字典形式好渲染
	params = {'client':'local','tgt':ctx['a2'], 'fun':'cmd.run', 'arg':ctx['b2']}   
	test = sapi.saltCmd(params)
	

        return HttpResponse(a22+"---hahaha---"+b22)
        
     #return render(request, "get_post.html", ctx)  # ctx字典渲染进去，模板出现键 不出现值
