#coding:utf8

from django.contrib.auth.models import User, Group
from rest_framework import serializers


#值得注意的是, 我们使用的是HyperlinkedModelSerializer.
#  你可以使用主键或者其他关系,
# 但使用HyperlinkedModelSerializer是一个好的 RESTful 设计.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')