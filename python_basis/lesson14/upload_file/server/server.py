# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : server.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-27 21:23:32
 @ desc       : 
***********************************************
"""
import socket,os

sk = socket.socket()

ip_port = ('127.0.0.1',13000)
sk.bind(ip_port)

sk.listen(5)

def post_file(sk_obj,path):
    '''
    上传文件
    :param sk_obj:
    :param path:
    :return:
    '''
    # 获取发送文件的大小
    file_size = os.stat()
    pass


def get_file():
    pass