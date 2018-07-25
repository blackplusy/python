#coding=utf-8
class animal:
	def jiao(self):
		pass

class dog(animal):
	def jiao(self):
		print('旺旺旺')

class cat(animal):
	def jiao(self):
		print('喵喵')


def test(obj):
	obj.jiao()

a=animal()
a.jiao()

d=dog()
c=cat()

test(d)
test(c)
