（1）
V1 没有使用装饰器 出自虫师博客.只是做了跳转，能访问的界面还是可以访问


（2）V2 版本使用装饰器更加完善

在django项目中，经常会看到下面这样的代码：

from django.contrib.auth.decorators import login_required  
 
@login_required  
def my_view(request):  
    ...  

里面有一个@login_required标签。其作用就是告诉程序，使用这个方法是要求用户登录的。
1.如果用户还没有登录，默认会跳转到‘/accounts/login/’。这个值可以在settings文件中通过LOGIN_URL参数来设定。（后面还会自动加上你请求的url作为登录后跳转的地址，如： /accounts/login/?next=/polls/3/ 登录完成之后，会去请求/poll/3）

2.如果用户登录了，那么该方法就可以正常执行