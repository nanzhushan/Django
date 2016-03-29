#coding:utf8
from django.db import models
from django.contrib import admin


#类名代表数据库表名,定义表格式
class BlogsPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

#将数据库的信息在后台admin显示，
#创建BlogPostAdmin类，继承admin.ModelAdmin父类，以列表的形式显示BlogPost的标题和时间。

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')


admin.site.register(BlogsPost,BlogPostAdmin)     ## 添加到后台，不加的话无法显示