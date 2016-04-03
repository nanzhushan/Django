#coding:utf8
from __future__ import unicode_literals
from django.shortcuts import render
from django.template.loader import render_to_string
import os
import json



#上下文渲染器


# Create your views here.

#返回字典在模板中使用,(常规方式)

def home(request):
    List = ['笑傲江湖', '渲染Json到模板']
    Dict = {'site': '笑傲江湖', 'author': '涂伟忠'}
    return render(request, 'home.html', {
            'List': json.dumps(List),
            'Dict': json.dumps(Dict)
        })

