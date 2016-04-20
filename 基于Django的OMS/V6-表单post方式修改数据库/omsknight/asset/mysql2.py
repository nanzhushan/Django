#coding:utf8
import MySQLdb
#查询操作

db = MySQLdb.connect("localhost","root","root","oms1" )
## 使用cursor()方法获取操作游标
cursor = db.cursor()

"""
sql = "SELECT COUNT(id) from asset_hostlist"
#执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()   ##是个元组
ss = str(results)
print ss[2]

"""



