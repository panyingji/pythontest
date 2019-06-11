# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : test.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-25 16:19:41
 @ desc       : 
***********************************************
"""

with open(r'D:\end.txt','r',encoding='GB2312') as f:
    ret = f.read()
    print(type(ret))
    print(ret)
    f.close()