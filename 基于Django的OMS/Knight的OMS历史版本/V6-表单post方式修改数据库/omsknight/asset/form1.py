#coding:utf8
#创建表单类处理表单
from django import forms
from asset.models import *

#
# class HostsListForm(forms.ModelForm):
#     class Meta:
#         model = HostList
#         widgets = {
#           'ip': forms.TextInput(attrs={'class': 'form-control'}),
#           'hostname': forms.TextInput(attrs={'class': 'form-control'}),
#           'product': forms.TextInput(attrs={'class': 'form-control'}),
#           'application': forms.TextInput(attrs={'class': 'form-control'}),
#           'idc_jg': forms.TextInput(attrs={'class': 'form-control'}),
#           'status': forms.TextInput(attrs={'class': 'form-control'}),
#           'remark': forms.TextInput(attrs={'class': 'form-control'}),
#         }



class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    name = forms.CharField()
