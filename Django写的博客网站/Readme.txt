(1)Django使用数据库的API 进行数据库的增删改差的原因:

注解;Django的数据库api 就是用Django特用的数据库的语法 可以操作所有的数据库。（也可以理解成使用DJango的模型而不是 import MySQLdb进行十几块的操作）,而是采用 from django.db import models  框架的模型


在视图中进行数据库查询的笨方法

正如第三章详细介绍的那个在视图中输出 HTML 的笨方法（通过在视图里对文本直接硬编码HTML），在视图中也有笨方法可以从数据库中获取数据。 很简单： 用现有的任何 Python 类库执行一条 SQL 查询并对结果进行一些处理。

在本例的视图中，我们使用了 MySQLdb 类库（可以从 http://www.djangoproject.com/r/python-mysql/ 获得）来连接 MySQL 数据库，取回一些记录，将它们提供给模板以显示一个网页：

#coding:utf8
from django.shortcuts import render_to_response    #数据用于渲染到html页面即可
import MySQLdb

def book_list(request):
    db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
    cursor = db.cursor()  #定义游标
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html', {'names': names})

这个方法可用，但很快一些问题将出现在你面前：

我们将数据库连接参数硬行编码于代码之中。 理想情况下，这些参数应当保存在 Django 配置中。

我们不得不重复同样的代码： 创建数据库连接、创建数据库游标、执行某个语句、然后关闭数据库。 理想情况下，我们所需要应该只是指定所需的结果。

它把我们栓死在 MySQL 之上。 如果过段时间，我们要从 MySQL 换到 PostgreSQL，就不得不使用不同的数据库适配器（例如 psycopg 而不是 MySQLdb ），改变连接参数，根据 SQL 语句的类型可能还要修改SQL 。 理想情况下，应对所使用的数据库服务器进行抽象，这样一来只在一处修改即可变换数据库服务器。 （如果你正在建立一个开源的Django应用程序来尽可能让更多人使用的话，这个特性是非常适当的。）

正如你所期待的，Django数据库层正是致力于解决这些问题。 以下提前揭示了如何使用 Django 数据库 API 重写之前哪个视图。

from django.shortcuts import render_to_response
from mysite.books.models import Book

def book_list(request):
    books = Book.objects.order_by('name')
    return render_to_response('book_list.html', {'books': books})
我们将在本章稍后的地方解释这段代码。 目前而言，仅需对它有个大致的认识。

(2) 完整的解释和操作链接:

http://docs.30c.org/djangobook2/chapter05/


不过个人觉得 不用用到其他数据库 还是直接用原生的import mysqldb吧 简单不用学它特有的数据库的api操作方法，它特有的数据库api的操作方法估计也难以实现复杂的sql语句和 存储过程的编写.