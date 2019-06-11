# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : socket_client.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-27 20:31:19
 @ desc       : 
***********************************************
"""
import socket

ip_port = ('127.0.0.1',13000)
# 创建客户端的socket对象
sk = socket.socket()

# 发起连接
sk.connect(ip_port)

sendData = input("请输入向服务器发送的内容>>>")
# 发送消息
sk.sendall(bytes(sendData,encoding='utf8'))

# 接收数据
server_data = sk.recv(1024)
print(f"服务器回复的内容为：{str(server_data,encoding='utf8')}")