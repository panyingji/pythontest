# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : decorator1.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-25 17:44:55
 @ desc       : 被装饰的函数不带参数
***********************************************
"""

# ===============================功能与装饰器相同================================
def outter(func):
    def inner():
        return func() + "!!!!"
    return inner

def hello():
    return "hello"

inner = outter(hello)
strr = inner()

print(strr)


# =================================装饰器的应用==================================

def outter1(func1):
    def inner1():
        return func1() + "!!!!"
    return inner1

@outter1   # 声明装饰器
def hello1():
    return "使用了装饰器"

def hi1():
    return "没有使用装饰器"

print(hello1())         # 有了装饰器的调用方式


# 没有装饰器的调用方式
inner1 = outter1(hi1)
hii = inner1()
print(hii)