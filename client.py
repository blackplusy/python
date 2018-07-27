#coding=utf-8
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.connect(('127.0.0.1',8081)) #绑定手机卡

#发，收消息
while True:
    msg=input('>>: ').strip()
    if not msg:continue   #若不加此句，当输入为空时，会在服务端接收时陷入死循环
    phone.send(msg.encode('utf-8'))
    data=phone.recv(1024)
    print('server back res:<%s>' %data)

phone.close()