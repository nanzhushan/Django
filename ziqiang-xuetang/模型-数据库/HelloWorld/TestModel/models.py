#coding:utf-8
# models.py
from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=20)