#coding:utf8
from django.db import models

# Create your models here.

class Xx_Tab(models.Model):

    pk_id = models.AutoField(primary_key=True)

    xx_id = models.IntegerField()

    xx_name = models.CharField(max_length=200)