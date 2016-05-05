#coding:utf8
##方法一
t = "true"
a =  [12,4,6,88]
b = [12,3,6,88,99]

for i in a:
    if i not in b:
        t = "false"


print t


