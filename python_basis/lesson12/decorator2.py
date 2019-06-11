# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : decorator2.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-25 18:34:37
 @ desc       : 被装饰的函数带参数
***********************************************
"""

def endsign(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs) + ' !!'
    return wrapper

@endsign
def hello(arg1,arg2=''):
    return 'hello %s,%s'% (arg1,arg2)

def goodbye(arg1,arg2=''):
    return 'goodbye {}{}'.format(arg1,arg2)

print(hello('小米','华为'))

hello = endsign(hello)
print(hello("中兴"))

print(goodbye('LEONE'))