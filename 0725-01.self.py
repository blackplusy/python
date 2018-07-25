#coding=utf-8
class student:
	def __init__(self,name):
		self.name=name
	def info(self):
		print('您的名字是%s'%self.name)

def studentinfo(student):
	student.info()
#heygor是student类的实例化
heygor=student('simida')
#对象实例化之后可以使用类中的方法
#studentinfo括号中传入的heygor是一个已经实例化的对象，可以调用类中的方法
studentinfo(heygor)

o8ma=student('o8ma')
studentinfo(o8ma)

