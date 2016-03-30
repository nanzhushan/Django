#coding:utf8
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogsPost
#from django.core.context_processors import csrf   #使用Django表单类提交，这行注释
from django.shortcuts import render_to_response
from .forms import AddForm   #引入表单类设计表单


# Create your views here.
def archive(request):
    posts = BlogsPost.objects.all()    #获取数据库里面所拥有BlogsPost对象
    t = loader.get_template("archive.html")          #通过模板名加载模板
    c = Context({'posts':posts})
    # return HttpResponse("这是博客首页")
    return HttpResponse(t.render(c))        #渲染到archive.html上,并展现

##get 请求,跳转到index的页面,templates下的index.html的action 动作用来处理get之后的内容
def index(request):
    return render(request,'index.html')

#使用Django的表单类处理post类型

def indexp(request):
    if request.method == 'POST':# 当提交表单时

        form = AddForm(request.POST) # form 包含提交的数据

        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            cc = "post方式相加的值是:  " + str(int(a) + int(b))
            return HttpResponse(cc)

    else:# 当正常访问时
        form = AddForm()
    return render(request, 'indexp.html', {'form': form})



##处理表单页面的加法
#request.GET 可以看成一个字典，
# 用GET方法传递的值都会保存到其中，
# 可以用 request.GET.get('key', None)来取值，没有时不报错

def add(request):
    a = request.GET['a']   #表单提交的a,介绍get方法传过来的a值，
    b = request.GET['b']   #表单提交的b
    a = int(a)   #转换成数字整型
    b = int(b)
    d = "返回a值: "+ str(a)
    return HttpResponse(d)

    # return HttpResponse("这是add的方法")



