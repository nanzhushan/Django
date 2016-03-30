#coding:utf8
#models定义数据库的信息

from django.db import models
from django.contrib import admin


#类名代表数据库表名,定义表格式
class BlogsPost(models.Model):                                 #BlogsPost继承父类models.Model
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    # ip = models.CharField(max_length=150)

#将数据库的信息在后台admin显示，
#创建BlogPostAdmin类，继承admin.ModelAdmin父类，以列表的形式显示BlogPost的标题和时间。

class BlogPostAdmin(admin.ModelAdmin):           #括号里是父类
    # list_display = ('title','timestamp')   #后台页面显示着两项
    list_display = ('id','title','timestamp')   #后台页面,按列表的先后顺序写的

#尝试在数据库里添加一栏



# admin.site.register(BlogsPost,BlogPostAdmin)     ## 添加到后台，不加的话无法显示
admin.site.register(BlogsPost,BlogPostAdmin)     ## 添加到后台，不加的话无法显示