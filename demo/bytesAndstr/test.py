# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : test.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 20:04:30
 @ desc       : 
***********************************************
"""
a = ord('我')
b = chr(25105)
c = b'\xe6\xbd\x98\xe8\x8b\xb1\xe5\x9f\xba'
d = "中国"
# 编码和解码的需要保持一致
e = d.encode("utf8")
f = e.decode("utf8")
print(a)
print(b)
print(e)
print(f)
# print(c.decode("utf8"))
# print(c.decode("gbk"))