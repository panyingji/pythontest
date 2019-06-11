# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : function.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-25 16:55:16
 @ desc       :
***********************************************
"""
# ==============================函数内部定义函数======================================
def foo():
    def bar():
        print("内部函数")
    bar()
    print("外部函数")
    return bar

bar = foo()
print(type(bar))


def foo1():
    def bar1():
        print("内部函数")
    print("外部函数")
    return bar1 # 此处不能有括号

# 使用内部函数的写法有两种
# 1、用变量接收外部函数的返回值（实际上就是返回内部函数的函数名）
# 2、直接用外部函数调用

# 写法1
bar1 = foo1()
bar1()

# 写法2
foo1()()







# =====================================函数内部定义类================================================

def outer():
    class Inner:
        def __init__(self):
            self.age = 20
            self.weight = 80
            print("init inner!")
    print("in outer!")
    return Inner

# 写法1
inner = outer()
inner()

# 写法2
inner = outer()()





# ===========================内部函数调用外部函数的变量===========================

def exitfun():
    var = '外部函数的变量'
    def innerfun():
        print(var)
    print('外部函数')
    return innerfun
exitfun()()