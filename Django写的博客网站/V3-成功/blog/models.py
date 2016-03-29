#coding:utf8
from django.db import models
from django.contrib import admin

# Create your models here.

#设计数据库
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()


#创建BlogPostAdmin类，继承admin.ModelAdmin父类，以列表的形式显示BlogPost的标题和时间
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(BlogsPost,BlogPostAdmin)