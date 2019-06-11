# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : test_os.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-25 13:09:52
 @ desc       : 
***********************************************
"""
import os

#os.system("mspaint")
#print('after call')
# 阻塞性调用
retcode = os.system("ipconfg")

if retcode == 0:
    print("cmd success!")
else:
    print("cmd fail!")