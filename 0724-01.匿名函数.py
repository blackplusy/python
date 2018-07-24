#coding=utf-8

def operation(a,b,opt):
	re=opt(a,b)
	return re

num1=int(input('数字1'))
num2=int(input('数字2'))
result=operation(num1,num2,lambda a,b:a+b)
print(result)


print('------------华丽的分割线-------------')
student=[{'name':'tom'},{'name':'jerry'},{'name':'snoppy'}]
student.sort(key=lambda x:x['name'])
print(student)
