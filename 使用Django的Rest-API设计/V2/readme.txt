完成了在Django框架models.py文件中定义了xx_tab表的相关信息，我们就可以用django命令来生成表。

python manage.py makemigrations xx_tab

注意：xx_tab是app名，此命令会在xx_tab app下migrations目录下生成一个0001_initial.py文件，此文件定义了建表信息，如果发现表定义有问题，在修改models.py中的定义后，需要删除0001_initial.py文件，重跑python manage.py makemigrations xx_tab，重新生成0001_initial.py。
执行python manage.py migrate xx_tab，在数据库中生成xx_tab表。
打开Sqlite数据库，在windows下可用
d:\dt\sqlite\sqlite3.exe db.sqlite3 打开当前的数据库，sqlite3.exe可在网上下载。
.table可查看当前的表。
.schema tab_name 可查看表结构定义。