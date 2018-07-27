#coding=utf-8
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #就是它，在bind前加
phone.bind(('127.0.0.1',8081)) #绑定手机卡
phone.listen(5) #开机

print('starting...')
while True: #链接循环
    conn,client_addr=phone.accept() #等电话 （链接，客户的的ip和端口组成的元组）
    print('-------->',conn,client_addr)

    #收，发消息
    while True:#通信循环
        try:   #加上的原因是因为在进行连接循环时，若此时连接的客户端断开，conn连接断开，收不到data报错，程序会中断，其他客服端的信息就传就不进来
            data=conn.recv(1024)
            # if not data:break  #针对linux
            print('client data: <%s>' %data)
            conn.send(data.upper())
        except Exception:
            break
    conn.close() #挂电话
phone.close() #关机