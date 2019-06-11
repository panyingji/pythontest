# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : test01.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       :
***********************************************
"""

def func(a, *args, b=3):
    print(a, *args, b)


func(1, b=8)

# print(1,2,3,4,5,6,7,8)
