#coding:utf8

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
