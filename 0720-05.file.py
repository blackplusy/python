#coding=utf-8

file=open('/home/heygor/0720/log','r')
for i in file.readlines():
	#print(i)
	#i=i.strip('\n') #去除内容中的回车
	b=i.split(' ')  #按照空格分割
	#print(type(b))
	print(b)
	if b[-1]=='18028768679':
		print('电话在文件中')
	else:
		print('不再文件中')
		
file.close()

print('***********')
file=open('/home/heygor/0720/log','a')
file.write('\nsimida   119')
file.close()

print('***********')
