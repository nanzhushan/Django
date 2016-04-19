#coding:utf8

from django.forms import ModelForm
from jlpt.models import ExamInfo


class ExamInfoForm(ModelForm):
    class Meta:
        model = ExamInfo
        fields = '__all__'