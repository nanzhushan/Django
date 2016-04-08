#coding:utf8
#/usr/bin/python
#python向shell传递变量
import os

a22 = "192.168.2.92"
os.environ['a22']=str(a22)
#os.system("salt $a22 cmd.run 'touch /root/331.txt'")

b22 = "touch /root/33344.txt"
os.environ['b22']=str(b22)

os.system('salt $a22 cmd.run "$b22"')       ##python的变量传到shell中,最外面使用单引号

#print os.system('echo $b22')
