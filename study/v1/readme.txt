（1）djangon渲染必须构造成字典形式

http://djangobook.py3k.cn/appendixH/

HttpRequest类是一个封闭HTTP提交信息的类型,而封闭HTTP输出信息的类型就是HttpResponse类,使用HttpResponse类可以实现三种类型的输出,即文本,URL,二进制流.
  实现这三类的属性和方法分别介绍如下:
1.文本的输出,在日常开发中,后台中的文本可能需要输出到浏览器中,让用户浏览,这就需要实现动态HTML的输出,使用HttpResponse类的Write静态方法可以实现,例如希望在浏览器上显示一个"hello world!"的字样时,可以在Page_load方法中增加如下代码,就可以实现:
  Response.write("hello world!")
2.URL的输出,程序开发经常需要根据情况将用户浏览的界面重定向到其他页面,例如,用户在没有登录的状态下查看自己的信息,系统需要首先将其转向到登录页,登录后再转回信息浏览页,实现URL的输出可以使用HttpResponse类的redirect方法实现,代码如下:
  response.redirect("http://www.djjwz.com/")
3.二进制流,有时需要将服务器上的文件提供给用户下载,或者在浏览器端动态生成一幅图片,例如,验证的初一二进制流输出到用户浏览器中.