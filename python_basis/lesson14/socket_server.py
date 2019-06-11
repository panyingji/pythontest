# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : socket_server.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-27 20:31:04
 @ desc       : 
***********************************************
"""
import socket

ip_port = ('127.0.0.1',13000)

# 创建一个用来与客户端建立连接的socket对象sk
sk = socket.socket()

# 绑定IP地址和端口号
sk.bind(ip_port)

# 监听请求
sk.listen(5)
print("Sever is waiting...")

# 等待传入连接
# 连接成功之后，返回一个新的套接字和客户端的地址
# 返回的conn，用来与客户端进行交流
conn,addr = sk.accept()
print(f"客户端的IP地址为：{addr}")


#接收数据
client_data = conn.recv(1024)
print(f"客户端发送的内容为：{str(client_data,encoding='utf8')}")

sendData = input("请输入向客户端发送的内容>>>")
# 发送数据给客户端
conn.sendall(bytes(sendData,encoding='utf8'))


conn.close()
sk.close()