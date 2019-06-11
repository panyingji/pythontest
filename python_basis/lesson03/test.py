# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : test.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       :
***********************************************
"""

# info = [1,2,3,4,5,6,7]
# print(info[::-1])
#
# a = 66666
# b = 66666
#
# print(id(a),id(b))
#
# print(info[-1:-8:-1])
#
# if ' ':
#     print('执行了')


def product():
    print(u'{}x{}={}\t'.format(i, j, i * j), end='')


for i in range(1, 10):
    for j in range(1, i + 1):
        product()
    print()
