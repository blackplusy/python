#coding=utf-8
def animal(pet1,pet2):
	print(pet1+'wang!!!'+pet2+'miao')

animal('dog','cat')
animal('heygor','simida')

print('______________________')

def animal(pet1,pet2):
	print(pet1+'wang!!!'+pet2+'miao')
animal(pet2='mimi',pet1='erha')
print('______________________')

def animal(pet2,pet1='erha'):
	print(pet1+'wang!!!'+pet2+'miao')

animal('波斯')
animal('pig','out man')

print('--------------------')
def test(x,y,*args):
	print(x,y,args)

test(1,2,'heygor','ladeng','sadamu')


print('_______________')
def test1(x,y,**kwargs):
	print(x,y,kwargs)

test1(1,2,a=10,b='heygor')
