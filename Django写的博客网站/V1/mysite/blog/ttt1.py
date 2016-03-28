#coding:utf8
#这里可以写sql语句

from django.db import models
from django.contrib import admin

import sqlite3

###
list_display = ('title','timestamp')
# print list_display

cx = sqlite3.connect("D:/pycharm/mysite/db.sqlite3")    #打开数据库
cu=cx.cursor()   #使用游标

dd = cu.execute("select * from blog_blogspost")
dd1 = cu.execute("SELECT id FROM blog_blogspost")
dd2 = cu.execute("SELECT title from blog_blogspost")
# print type(dd)
print dd1.fetchall()
dd21 = dd1.fetchall()
print type(dd21)    #list类型
print dd21

id3 = 356


#print type(dd21)

ff = cu.fetchall()   #fetch函数 获取结果集
#print ff
# print type(ff)
# print ff[0]


