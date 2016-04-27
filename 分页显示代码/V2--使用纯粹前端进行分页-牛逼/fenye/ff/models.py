#coding:utf8
from django.db import models

# Create your models here.

#设计数据库
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()