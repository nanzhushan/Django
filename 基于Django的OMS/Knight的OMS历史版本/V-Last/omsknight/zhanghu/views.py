#coding:utf8
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.template import RequestContext
from django import forms
from django.contrib.auth.decorators import login_required

from django.contrib import auth

from django.contrib.auth.decorators import login_required   ##添加登录认证

# Create your views here.


#定义表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


## 定义login的函数方法
def login(req):

    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():                          ##校验用户名和密码
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与dj字典的auth表进行比较
            # user = User.objects.filter(username=username,password=password)        # 改成自己建立的用户表作登录验证
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
            # if user is not None:
                auth.login(req, user)
                # req.session['username'] = username  # 并且写入session
                # return  HttpResponseRedirect('/zhanghu/success/')       #跳转到登录之后的页面
                return HttpResponseRedirect('/hindex/')  # 跳转到登录之后的页面

            else:
                return HttpResponse(u'登录失败,请检查用户名和密码...')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

################
#登录之后跳转页
def success(request):
    username = request.session.get('username', '')
    return render_to_response('success.html',{'username':username})

########################
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponse(u'成功退出，使用django自带的后台退出')


######使用django的后台session,成功实现
@login_required
def list3(request):
    if request.user.is_authenticated():          ## 如果已经验证成功通过
        return render_to_response('list3.html')
