#coding:utf8
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

# Create your views here.
'''
在django_rest_framework中, 所有常见的行为都被归到了ViewSets中.
当然我们可以将这些行为分拆出来, 但使用ViewSets, 使view的逻辑更为清楚.
使用queryset和serializer_class代替model变量,
使我们能更加好的控制API行为, 这也是我们推荐的使用方式
'''



class UserViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑user 的 API endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑group的 API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

