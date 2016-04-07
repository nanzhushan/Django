##注意指定安装Django的版本
（sudo) pip install Django
或者 (sudo) pip install Django==1.6.10 或者 pip install Django==1.7.6

(sudo) pip install --upgrade pip


学习一段时间的web.py  看了一些demo ，用web.py可以写自己的博客了但是没有后台。
现在回头来看Django 看得懂了。看来初学者学习web.py然后再看Django是个不错的选择.

或者也可以学习web2py 一站式解决方案 ，不过web2py的资料好少，
website:http://www.cnblogs.com/linjiqin/p/3595891.html

安装Django，使用pip install Django 安装即可, 并将 D:\Python27\Scripts 加入环境变量

(1)创建第一个项目

django-admin.py startproject HelloWorld                    #创建项目

python manage.py startapp oms

python manage.py runserver 0.0.0.0:8001                    #启动服务

python manage.py dbshell  #数据库命令行

python manage.py shell   #python项目终端

python manage.py  可以查看更多命令

python manage.py migrate  #创建数据库，没有定义数据库驱动默认是SQLite

python manage.py createsuperuser  #创建后台admin账号

注意:syncdb  是Django1.7之前的版本，之后的版本用migrate代替


（2）eclips创建Django项目: file-new-other-Pydev Django Project即可，记住project不能有种横杠.


(3)不错的Django博客源码:
http://www.cnblogs.com/fnng/p/3737964.html



网上搜索 发现Django 和flask的文章好多 但是web.py的很少.Django还有后台功能，初学者还是学习Django吧。
多看看人家的源码 然后照着写.


web.py很轻 可以随意扩展 所以什么都要自己造轮子.豆瓣网就是用的web.py