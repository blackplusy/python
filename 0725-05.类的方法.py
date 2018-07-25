#coding=utf-8

class people:
	country='china'
	@classmethod
	def getcountry(cls):
		return cls.country

p=people()
print(p.getcountry()) #实例对象调用类的方法
print(people.getcountry())#类对象调用类的方法


class people:
	country='china'
	@classmethod
	def getcountry(cls):
		return cls.country
	@classmethod
	def setcountry(cls,country):
		cls.country=country

p=people()
print(p.getcountry())
print(people.getcountry())
p.setcountry('USA')
print(p.getcountry())
print(people.getcountry())
