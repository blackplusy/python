#coding=utf-8
def jia(x,y):
	return 'x+y= %d'%(x+y)

def jian(x,y):
	return x-y

def cheng(x,y):
	return x*y


a=int(input('输入第一个数字'))
b=input('输入运算符')
c=int(input('输入第二个数字'))

if b=='+':
	e=jia(a,c)
	print(e)
elif b=='-':
	e=jian(a,c)
	print(e)
