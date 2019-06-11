# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : StrAndBytes.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       : 字符串与字节串相互转换
***********************************************
"""

a = b"Hello, world!"   # bytes object
b = "Hello, world!"    # str object


# 字符串转字节  str --> bytes
print(str.encode(b))  # 默认 encoding="utf-8"
print(bytes(b, encoding="utf8"))
print(b.encode())      # 默认 encoding="utf-8"


# 字节转字符串  bytes --> str
print(bytes.decode(a))   # 默认encoding="utf-8"
print(str(a, encoding="utf-8"))
print(a.decode())       # 默认 encoding="utf-8"