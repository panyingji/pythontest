# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : HomeWork.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       :
***********************************************
"""

def getName(srcStr):
    strList = srcStr.split(', ')    # 以 逗号+一个空格 的格式切割原始字符串，并返回列表strList
    str1 = str(strList[1])          # 将strList中指定不变格式的部分强制转为字符串str1
    finall_list = str1.split(' ')   # 以 一个空格 的格式切割提取出来的字符串，并返回列表finall_list
    return finall_list[-1]


name = getName('A old lady come in, the name is Mary, level 94454')
print(name)