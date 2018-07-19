#coding=utf-8
#直接访问
li=['heygor','yueyue','shengsheng']
print(li)
#遍历访问
for i in li:
	print(i)
#成员访问
print('heygor' in li)

print(li[0])
print(li[-2])
#print(li[5])

print(li[:-1])
print(li[1:])
print(li[1:2])

li=[1,2,3]
li2=[4,5,6]
print(li+li2)
print('************')
li=[1,2,3]
print(li)
li[2]=100
print(li)
li[-1]=30
print(li)
print('************')

li=['a','b','c']
print(li)
del li[1]
print(li)


li2=[1,2,3,4,5,6]
li2.append('memeda')
print(li2)
print('************')
