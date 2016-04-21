#coding:utf8
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.template import RequestContext
from django import forms
from models import User

from django.contrib.auth.decorators import login_required   ##添加登录认证
from django.contrib.auth import authenticate, login


# Create your views here.

##authenticate(username,password)函数需要两个参数username，password，
# 如果校验通过则返回User对象，如果校验不通过返回None
'''
user = authenticate(username='john', password='secret')
if user is not None:
    if user.is_active:
        print "You provided a correct username and password!"
    else:
        print "Your account has been disabled!"
else:
    print "Your username and password were incorrect."
'''




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

############登陆
'''
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
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                # return HttpResponseRedirect('/online/login/')
                return HttpResponse(u'登录失败,请检查用户名和密码...')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

'''



##################################################
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
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                # return HttpResponseRedirect('/online/login/')
                return HttpResponse(u'登录失败,请检查用户名和密码...')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))



#################################################################################
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
@login_required(login_url='/online/')

def list(request):
    return HttpResponse(u"这是list的页面....")
    # return HttpResponse(u'这是list页面来测试是不是需要通过登录才能进行访问....')



# @login_required
# def myview(request):
#     return render_to_response('11.html')


