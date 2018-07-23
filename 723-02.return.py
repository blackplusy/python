#coding=utf-8
def sum1(a,b):
	suan=a+b
	return suan

s=sum1(20,30)
print(s)


def re(a,b):
	a*=10
	b*=10
	return a,b
num=re(3,5)
print(type(num))
print(num)
r1,r2=re(3,4)
print(r1,r2)
