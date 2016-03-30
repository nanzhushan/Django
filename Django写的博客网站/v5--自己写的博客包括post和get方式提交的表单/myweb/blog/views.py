#coding:utf8
from django.shortcuts import render
from django.template import loader,Context,RequestContext
from django.http import HttpResponse
from blog.models import BlogsPost
#from django.core.context_processors import csrf


from django.shortcuts import render_to_response

# Create your views here.
def archive(request):
    posts = BlogsPost.objects.all()    #获取数据库里面所拥有BlogsPost对象
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})
    # c = RequestContext(request,{'posts':posts})   #和上面的等价
    # return HttpResponse("这是博客首页")
    return HttpResponse(t.render(c))        #渲染到archive.html上

##get 请求,跳转到index的页面
def index(request):
    return render(request,'index.html')

def indexp(request):
    return render(request,'indexp.html')

##处理表单页面的加法
#request.GET 可以看成一个字典，
# 用GET方法传递的值都会保存到其中，
# 可以用 request.GET.get('key', None)来取值，没有时不报错

def add(request):
    a = request.GET['a']   #表单提交的a,介绍get方法传过来的a值，
                            #所以多个get用不同的值区分
    b = request.GET['b']   #表单提交的b
    a = int(a)   #转换成数字整型
    b = int(b)
    # return HttpResponse(str(a+b))
    return  HttpResponse(a)  #返回a的值

    # return HttpResponse("这是add的方法")

##定义post提交的函数
#表格后面还有一个{% csrf_token %}的标签。
# csrf全称是Cross Site Request Forgery。这是Django提供的防止伪装提交请求的功能。
#POST方法提交的表格，必须有此标签
def addp(request):
    ctx = {}      #定义空字典,必须是字典形式
    # ctx.update(csrf(request))  #可以使用也可以不使用csrf，但是模板标签上必须指定 {% csrf_token %}
    if request.POST:   #如果有post值,必须是字典形式
        # ctx['a1'] = request.POST['a']  #字典里插入data
        ctx['a1'] = int(request.POST['a'])  #字典里插入data
        ctx['b1'] = int(request.POST['b'])   #post提交的是str类型，所以要转换,用int转换
        ctx['c1'] = ctx['a1']+ ctx['b1']

    return render(request,"indexp.html",ctx)    #ctx字典渲染进去，模板出现键 不出现值

    # return HttpResponse(a)    #返回a的值