#coding:utf8
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.template import RequestContext
from django import forms
from models import User

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

#登陆
def login(req):

    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():                          ##校验用户名和密码
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:

                #比较成功，跳转index
                response = HttpResponseRedirect('/online/index/')
                #将username写入浏览器cookie,失效时间为3600,登录成功才写入cookies，方便后面判断有没有username的cookie 才让其访问子页面
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                # return HttpResponseRedirect('/online/login/')
                return HttpResponse(u'登录失败,请检查用户名和密码...')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

#登陆成功
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response


#因为在online的view上添加了@login_required(login_url="/online/login/")，所以当访问home页面时，如果没有登陆，则自动跳转到登陆页面．
# @login_required(login_url='/online/')

def list(req):
    username = req.COOKIES.get('username','')            #读取cookies
    # return HttpResponse(username)
    if username:                                   #如果有cookies 就返回,有说明之前成功登录写入cookies过.
        return render_to_response('list.html')
    else:
        #return HttpResponse(u"没有检测到cookies，cookies 的实效时间是3600秒，请重新登录..")
		return HttpResponseRedirect('/online/')   #返回到登录页面

