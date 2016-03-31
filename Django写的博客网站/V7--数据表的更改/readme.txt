对于Django1.9之前的，

首先 

(1)python manage.py syncdb  创建里DJango自带的后台的一些表.


(2)然后通过 python manage.py makemigrations blog  更新模型里的数据表

Django 1.7之后,增加了类似South的migration功能，修改Model后可以在不影响现有数据的前提下重建表结构。
这是目录下会增加 migrations，记录表的更改.

(3)然后同步模型到数据库的数据.
python manage.py syncdb 

（4）

我们再次创建一个表试一试.

在models里面定义表.然后使用python manage.py makemigrations blog

最后 python manage.py syncdb  看数据库成功了.

原来blog_blogspost  的表也没有删除.


########################################################
###对于1.8.2  python manage.py migrate 等价于 python manage.py syncdb

注意：
# 进入包含有 manage.py 的文件夹
python manage.py syncdb
 
注意：Django 1.7及以上的版本需要用以下命令
python manage.py makemigrations
python manage.py migrate
#########################################################


我们会想为什么一定要同步model和数据库了？
原因:

(1)以Django的orm为例， 你只用维护model的定义， 然后makemigrations，
migrate/syncdb就可以把对model的更改同步到数据库.

(2)如果采用直接客户端工具去 就要维护两个一个是mysql一个model，值维护一个后台不能用。

