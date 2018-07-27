#coding=utf-8
import socket #导入scoket模块

#以元组形式定义一个ip地址和端口
ip_port=('127.0.0.1',9999)

#创建对象并且绑定IP地址进行监听
sk=socket.socket()
#绑定地址到套接字
sk.bind(ip_port) 
#开始监听传入链接(可以挂起的最大连接数) 
sk.listen(5)

while True:
	print('server wating for u!!')
	#conn代表客户端和服务端建立连接后的通信线路
	conn,addr=sk.accept()#accpet代表阻塞式，没有收到连接请求就不会向下执行
	#接受客户端发来的信息
	client_data=conn.recv(1024)#recv也属于阻塞编程
	print(client_data)
	#回复消息
	conn.sendall(('server reviced your meeeage').encode())
	conn.close()
	

