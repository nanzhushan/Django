#coding:utf8
from django import forms
from models import *


##定义表单框内容，从而可在views中进行有效性检测

class MailForm(forms.Form):
    username = forms.CharField(label='用户名')
    email = forms.EmailField(label='电子邮箱')
