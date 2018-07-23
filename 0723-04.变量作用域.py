#coding=utf-8

def test1():
	a=10
	print('修改前',a)
	a=20
	print('修改后',a)

def test2():
	a=40
	print('test2中的a',a)

test1()
test2()


a=100
print('全局变量是a,',a)
def test1():
	print('test1中使用全局变量',a)

def test2():
	print('test2中使用全局变量',a)

test1()
test2()


print('------------华丽的分割线-------------')

a=10
print('全局变量a的值是',a)
def test01():
	a=20
	print('test01中a的值是',a)

def test02():
	print('test02中a的值是',a)

test01()
test02()

print('------------华丽的分割线-------------')
print('------------华丽的分割线-------------')
a=100
print('全局变量a的值',a)
def test1():
	global a
	a=200
	print('test1中修改全局变量a',a)

def test2():
	print('test2中使用你全局变量a',a)

test1()
test2()
print('全局变量a的值是',a)
