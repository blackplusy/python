#coding=utf-8
a=(1)
print(a)
print(type(a)) #打印变量a的数据类型
a=(1,)
print(a)
print(type(a)) #打印变量a的数据类型

#访问元组
tup=(1,2,3,4,5)
for i in tup:
	print(i)

#删除元组
tup=(1,2,3)
del tup
#print(tup)

tup=(1,2,3,4,5)
print(tup[0])
print(tup[-2])
print(tup[2:4])
print(tup[3:])
print(tup[:3])


tup=(1,2,3,4,3,2,8)
print(len(tup))
print(max(tup))
print(tup.index(8))
print(tup.count(2))

