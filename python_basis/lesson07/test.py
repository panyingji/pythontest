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

import pprint
# 字典定义
'''
1- 键：支持的类型(不可变的类型）：字符串、int、float、元组，不可以是 列表、字典

2- 值：任意类型

'''

'''
特性：
    1- 键唯一
    2- 若定义两个相同的键，则后面位置的键覆盖前面位置的键
    3- 字典可以修改key的值
    4- 字典增加键值对：dict1['age'] = 20 ，若键存在，则覆盖；若键不存在，则新增。
    5- 获取字典某个键对应的值：print(dict1[key])
    6- 若键不存在，则报错'KeyError:key'
    7- Python3语法----增加键值对的位置：尾部
    8- Python2语法----增加键值对的位置：随机
    9- 删除键值对：
        1- del dict[key]
        2- dict.pop(key)
        3- 没有remove方法
    10- 字典属于哈希，不是序列，没有下标
'''
dict1 = {}  # 定义空字典
dict2 = {'name': 'Tom'}
students = {
    'Mike': {
        'age': 25,
        'height': 180,
        'weight': 80,
        'nickname': 'mike'
    },
    'Tom': {
        'age': 20,
        'height': 180,
        'weight': 80,
        'nickname': 'tom'
    }
}
# print(students['Mike']['age'])   # 字典套字典的访问
#
# print('Mike' in students) # 判断键是否在字典里
# print()
#
# for one in students:     # 字典的遍历实际上就是遍历键
#     print(one)
#     print(students[one])

# 键值对---[(键,值),(键,值),(键,值),(键,值),(键,值)] --- 返回类列表，可以用for循环来遍历，但不能直接取下标
print(students.items())

for one in students.items():
    print(one)

# print(list(students.items()))
# print(list(students.items())[1])  # 转换成列表再采用下标取值
#
# for name, info in students.items():  # 相当于：for name,info in [(1,2),(3,4)]  ------键值对的使用
#     print(name, info)
#
# # 字典的完美打印,需要 import pprint
# pprint.pprint(students)
#
# # 清空字典
# # students.clear()
# # print(students)
#
# print(students.keys())  # 返回字典所有的键，为类列表，可以for循环遍历，但不可以下标取值
# print(students.values())  # 返回字典所有的值，为类列表，可以for循环遍历，但不可以下标取值
# print(students.items())  # 返回字典所有的键值对，为类列表，可以for循环遍历，但不可以下标取值
#
# # 增加字典元素
# # d = {'1': '2', '2': '3'}
# # d.update({'5': '6', '7': 8})
# # print(d)
