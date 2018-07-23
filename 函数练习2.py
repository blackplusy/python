#coding=utf-8
user1={'admin':'123','ladeng':'1456'}

def panduan(username,passwd):
	if username in user1.keys():
		if passwd==user1[username]:
			return '用户名密码正确'
	else:
		return '有问题！！'

username=input('请输入用户名：')
passwd=input('请输入密码')
res=panduan(username,passwd)
print(res)

	
