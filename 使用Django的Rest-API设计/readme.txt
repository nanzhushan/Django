学习链接:
https://blog.laisky.com/p/django-rest/


注意：Django 自带了api后台,比flask复杂点

安装方法:
pip install djangorestframework 

RESTful架构实际的6个原则:

1)Uniform Interface: 统一接口，（服务端和客户端通过统一接口进行通信，可以让客户端和服务端能独立升级）
2）Stateless： 无状态。（不依赖，客户端完全通过表现层实现）
3）Cacheable： 可缓存的
4） Client-Server： 客户端和服务端分离（客户端包含数据，服务端不包含用户状态）
5）Layered System: 分层系统
6）Code on Demand：按需编码，服务端和客户端都用统一的接口进行通信，所以服务端和客户端可以用自己喜欢的编程语言编写。


#########################
Django REST framework有很多种“用法”，最常见的用法是：

1. 定义资源。资源将python对象（比如model对象）进行隔离、组装，生成需要序列化（serialize)的数据。除了基本的Resource类型外，框架还提供了FormResource和ModelResource，以便于对Form或Model的处理。Resource有助于View中的处理，当然你也可以不使用Resource,而在View中去指定要序列化的数据。

2. 创建视图。视图是对django View的封装，并定义序列化、反系列化等方法，同时通过Mixin的支持来实现get,post,put,delete等操作。框架内置了ModelView，与ModelResource配合使用非常简单方便。

3. 定义url，将正则表达式匹配的View类的as_view方法，该方法会返回django的view函数。