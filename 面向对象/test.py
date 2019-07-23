# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : test.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-07-22 15:47:49
 @ desc       : 
***********************************************
"""
# class Foo(object):
#     def bar(self):
#         print("bar!")
#     def spam(self):
#         self.bar()
#         Foo.bar(self)
#
#
# Foo().spam()

class X(object):
    pass
class Y(X):
    pass
class Z(Y,X):
    pass
obj = Z()
print(type(obj))