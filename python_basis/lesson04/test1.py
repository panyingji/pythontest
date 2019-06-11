# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : test1.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       :
***********************************************
"""

def t2(para):
    para = 3


b = 'a'
t2(b)
print(b)


def t3(para):
    para[0] = 3


b = [1]
t3(b)
print(b)


def t4(para):
    para = 3


b = [1]
t4(b)
print(b)

print('my name is jack'.split(' ')[-1])