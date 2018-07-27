#coding=utf-8
import socket

ip_port=('127.0.0.1',9999)

sk=socket.socket()
#连接到address的套接字，如果连接出错，返回socket error
sk.connect(ip_port)
sk.sendall(('server server im client！！').encode())
server_reply=sk.recv(1024)
print(server_reply)
sk.close()
