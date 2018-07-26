#coding=utf-8
'''
arr=(x for x in range(1,6))
print(type(arr))
#for i in arr:
#	print(i)

print('----next1-----')
print(next(arr))
print('----next2-----')
print(next(arr))
'''
def createnum():
	print('开始生成器方法------')
	a,b=0,1
	for i in range(0,5):
		print('--step1--')
		yield b
		print('--step2--')
		a,b=b,a+b
		print('step3')
	print('stop!!!')

print('调用方法')
#print(createnum())

func=createnum()
x=next(func)
print(x)
		
func=createnum()
x=next(func)
print(x)

func=createnum()
x=next(func)
print(x)
