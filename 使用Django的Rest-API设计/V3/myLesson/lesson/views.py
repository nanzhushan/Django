#coding:utf8

from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from lesson.serializers import BoolSerializer
from lesson.models import Book


#reate your views here.

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONResponse().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONRenderer,self).__init__(content,**kwargs)


def book_list(request,num):
    if request.method == 'GET':
        # b = Book.objects.all()
        b = Book.objects.get(id=num)
        ser = BoolSerializer(b)
        return JSONResponse(ser.data)

