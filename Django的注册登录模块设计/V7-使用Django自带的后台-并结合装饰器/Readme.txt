使用Django自带的后台登录进行访问，核心代码如下：

if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():                          ##校验用户名和密码
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与dj字典的auth表进行比较
            user = auth.authenticate(username=username,password=password)
		.......
	
##########################################

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


###############################################################

