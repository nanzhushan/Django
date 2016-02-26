#coding:utf-8

#只不过 HttpResponse 是把内容显示到网页上。

from django.http import HttpResponse

# Create your views here.

def index(request):       #定义函数，传入参数
    return HttpResponse(u"欢迎光临knight的首页!")   #函数 返回了一个 HttpResponse 对象

#那问题来了，我们访问什么网址才能看到刚才写的这个函数呢？怎么让网址和函数关联起来呢？