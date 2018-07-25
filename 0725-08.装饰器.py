#coding=utf-8
import time
#定义一个函数打印hello，1s钟后打印world
'''
def func():
	print('hello')
	time.sleep(1)   #时间休眠一秒
	print('world')

func()
'''	
#增加功能：计算函数执行的时间

def jisuan(func):
	def zsq():
		startime=time.time()
		func()
		endtime=time.time()
		sec=endtime-startime
		print('时间是%d s'%sec)
	return zsq

@jisuan
#核心功能不能变
def func():
	print('hello')
	time.sleep(1)   #时间休眠一秒
	print('world')


f=func
f()
