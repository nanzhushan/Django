#coding:utf8

#这里主要写数据的序列化和反序列化

from lesson.models import Book
from rest_framework import serializers


class BoolSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)

    def restore_object(self,attrs,instance=None):
        if instance:
            instance.title = attrs['title']
            instance.name = attrs['name']
            instance.author = attrs['author']
            return instance

        return Book(**attrs)


