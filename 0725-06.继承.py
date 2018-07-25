#coding=utf-8
'''
class dog:
	def __init__(self,name,color='black'):
		self.name=name
		self.color=color
	def run(self):
		print('旺财在奔跑！！！')

class taidi(dog):
	def set_name(self,name):
		self.name=name
	def eat(self):
		print('im eating!!!')

gou=taidi('泰迪')
print('名字为：%s',gou.name)
print('颜色是：%s',gou.color)
gou.eat()
gou.set_name('erha')
print('狗狗的新名字',gou.name)
gou.run()
'''
'''
class a:
	def printa(self):
		print('-----a-----')

class b:
	def printb(self):
		print('---b---')

class c(a,b):
	def printc(self):
		print('----------c-----------')

c1=c()
c1.printa()
c1.printb()
c1.printc()

'''

class dog():
	def sayhi(self):
		print('wang!!!')

class fadou(dog):
	def sayhi(self):
		print('狗富贵，互相旺！！！！')

dog1=fadou()
dog1.sayhi()

