#coding=utf-8
import os
os.system('ls')  #运行系统中的命令
#os.remove()      #删除系统中文件
#os.getcwd()      #当前路径
print(os.listdir('/opt'))     #指定目录下所有文件和文件名
print(os.path.split('/var/log/syslog'))  #返回一个路径的目录和文件名
print(os.path.isfile('/var/log/syslog')) #判断是否是文件
#os.system('ifconfig')
#os.path.isdir()  #判断是否是目录
#os.path.exists() #判断存在性

