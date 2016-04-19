#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse

from jlpt.forms import ExamInfoForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ExamInfoForm(request.POST)
        exam_info = form.save()
        return HttpResponse(u'谢谢你的提交')
    else:
        form = ExamInfoForm()
    return render(request, 'mm.html', {'form_info': form})



