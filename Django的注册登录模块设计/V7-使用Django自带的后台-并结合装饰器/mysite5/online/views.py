#coding:utf8
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.template import RequestContext
from django import forms
from models import User
from django.contrib.auth.decorators import login_required

from django.contrib import auth

from django.contrib.auth.decorators import login_required   ##添加登录认证
# from django.contrib.auth import authenticate, login
# Create your views here.

#表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

#login模块重新，不查数据库直接，直接用django自带的后台登录的auth表
# 通过dj的字典的后台登录才算真正的登录，否则不算登录。

def login(req):

    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():                          ##校验用户名和密码
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与dj字典的auth表进行比较
            user = auth.authenticate(username=username,password=password)
            # if user is not None and user.is_active:
            if user is not None:
                return  HttpResponseRedirect('/online/index/')       #跳转到登录之后的页面
            else:
                return HttpResponse(u'登录失败,请检查用户名和密码...')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

#登录之后跳转页
def index(req):
    username = req.session.get('username','')
    return render_to_response('index.html' ,{'username':username})

#重新loggou的方法，使用django自带的后台登录进行退出.
def logout(request):
    auth.logout(request)

    return HttpResponse(u'成功退出，退出的是dj自带的auth模块')


#因为在online的view上添加了@login_required(login_url="/online/login/")，所以当访问home页面时，如果没有登陆，则自动跳转到登陆页面．
# @login_required(login_url='/online/')

#@login_required

##使用django自带的后台用户名和密码登录.

## 不使用装饰器的使用方法
def list(request):
##验证失败,跳到错误页面
    if not  request.user.is_authenticated():
        return HttpResponseRedirect('http://127.0.0.1:8000/static/login_error.html')
    else:
        return render_to_response('list.html')


#使用装饰器的方法
@login_required
def list2(request):
    return render_to_response('list2.html')

##验证失败,跳到错误页面,下面的方法和使用装饰器等效，使用装饰器只是更简单。使用下面的方法就去掉装饰器即可。
    # if not  request.user.is_authenticated():
    #     return HttpResponseRedirect('http://127.0.0.1:8000/static/login_error.html')
    # else:
    #     return render_to_response('list2.html')




