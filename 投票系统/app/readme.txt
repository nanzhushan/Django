学习链接:
http://www.tuicool.com/articles/VrUf6ba

'''
def __unicode__(self): 解析如下：

实现unicode()内嵌函数；
应该返回Unicode对象。当没有定义这个方法时，
取而代之的是string转换，转换的结果是用系统默认编码转化为Unicode。
##########################
__unicode__()方法是在一个对象上调用unicode()时被调用的。
因为Django的数据库后端会返回Unicode字符串给model属性，
所以我们通常会给自己的model写一个__unicode__()方法。前面的例子也可以更简单地写成：

class Person(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)

     def __unicode__(self):
         return u'%s %s' % (self.first_name, self.last_name)
如果定义了__unicode__()方法但是没有定义__str__()方法，
Django会自动提供一个__str__()方法调用__unicode__()方法，然后把结果转换为UTF-8编码的字符串对象。
在实际开发中，建议：只定义__unicode__()方法，需要的话让Django来处理字符串对象的转换。

'''


################

url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

解析如下：实际就是一个正则表达式.

##################################
三 matchobject
matchobject为re.search,re.match等匹配成功后返回的对象，包含了匹配的结果。
在正则表达式中，可以使用()来将部分正则表达式分组且编号，编号从1开始，使用数字来使用，例如1 2 3，(?p<name>)还可以给分组命名, 使用（？p=name）来使用命名的组。
matchobject.group()包含了所有匹配的内容，等价于matchobject.group(0)，此时的0表示所有的匹配；
matchobject.groups教程()包含了正则表达式中所有使用()定义的组对应的匹配内容；
matchobject.group(n)，表示返回正则表达式中的第n个组()匹配的内容，此时n不为0， 等价于matchobject.groups()[n-1];
matchobject.lastindex, 表示正则表达式中分组()的个数；

########################################################
