#coding:utf8
#创建表单类处理表单
from django import forms
from asset.models import *


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    name = forms.CharField()
