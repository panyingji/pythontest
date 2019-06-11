# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : decorator3.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-25 18:49:32
 @ desc       : 1、装饰器中自带参数，更加通用
                2、装饰器的本质是函数，在不改变
                   函数内部逻辑的前提下改变函数的
                   行为
***********************************************
"""

# ==========================装饰器中自带参数，更加通用=================================
def endsign(tail):
    def decorator(func):
        def wrapper(*args,**kwargs):
            return func(*args,*kwargs) + tail
        return wrapper
    return decorator

@endsign("@@@@@@@@@@")
def hello(arg1,arg2=''):
    return 'hello，{},{}'.format(arg1,arg2)

@endsign("~~~~~~~~~")
def goodbye(arg1,arg2=''):
    return f'goodbye，{arg1},{arg2}'

# 用装饰器的写法
print(hello("小明","小风"))
print(goodbye("小李"))

# 没有用装饰器的写法
# hello = endsign('666')(hello)
# strr = hello('小明，小强')
# print(strr)
