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

print('【----------文件的读写----------】')
'''
一、打开文件
    1、路径的写法（3种）
        fileDir = 'G:/test.txt'
        fileDir = 'G:\\test.txt'
        fileDir = r'G:\test.txt'   #r 取消转义
'''
print('【----------读文件----------】')
# fileDir = r'D:\Python Project\lesson06\lesson06\test.txt'
# file_object = open(fileDir,'r')
# print(file_object.tell())              # 获取文件指针的位置
# print(file_object.read())              # 默认读所有
# print(file_object.read(2))             # 指定长度读取文件
# print(type(file_object.read(2)))       # read()方法返回的是字符串str
# print(file_object.read().split('\n'))  # 分行读取
# print(file_object.tell())
# file_object.read(1)
# print(file_object.tell())
# file_object.seek(3,0)                      # 移动文件指针的位置,0模式，都是从绝对零点开始的，可缺省，只支持 'r'模式
# print(file_object.tell())
# file_object.seek(2,1)                      # 在当前位置开始移动，1模式，1不可缺省，必须要以'rb'模式打开
# print(file_object.tell())
# file_object.seek(-2,2)                     # 在字符串最后开始移动，2模式，2不可缺省，必须要以'rb'模式打开，可往前移动和往后移动
# print(file_object.tell())
# file_object.close()
# print(file_object.readline())              # 单行读取，两个readline读取两行
# print(file_object.readline())
# print(file_object.readlines())             # 一次性读取所有行，返回列表list，每一行为列表的一个元素
# print(file_object.read().splitlines())     # 去换行符用的 -----相当于split('\n')


print('【----------写文件 w模式 ----------】')
fileDir = r'D:\Python Project\lesson06\lesson06\test1.txt'
fo = open(fileDir, 'w')  # 1.如果文件不存在----会创建文件；2.如果文件存在-----清空打开；3.带返回值
fo.write('123456\nABCDEF\nabcdef')  # 只能写入内存，不能写入硬盘，Pycharm会自动关闭文件，所以才会写入
fo.flush()
fo.close()

print('【----------写文件 a模式 ----------】')
fo = open(fileDir, 'a')  # 1.如果文件不存在----会创建文件；2.如果文件存在-----清空打开；3.带返回值
fo.write('123456\nABCDEF\nabcdef')  # 只能写入内存，不能写入硬盘，Pycharm会自动关闭文件，所以才会写入
fo.flush()
fo.close()

print('【----------文件的读写模式：r+ w+ a+ ----------】')
print('r+ w+ a+的特点取决于r w a的特点，只不过是可读可写而已')

fileDir1 = r'D:\Python Project\lesson06\lesson06\test.txt'
print('【----------with...open...as----------】')
with open(fileDir, 'r') as rFile, open(fileDir1, 'w') as wFile:
    '''
    好处：
    1.可以同时操作多个文件
    2.可以省略close()
    '''
    print('此处写代码块')

# print('【----------9*9乘法表----------】')
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{}x{}={}\t'.format(i, j, i * j), end='')
#     print()


def t1(para1):
    para1 = 3
    print(id(para1))

b1 = 'a'
t1(b1)
print(id(b1))

def t2(para2):
    para2[0] = 3
    print(id(para2))


b2 = [1]
t2(b2)
print(id(b2))


def t3(para3):
    '''
    
    :param para3:
    :return:
    '''
    para3 = 3
    print(id(para3))


b3 = [1]
t3(b3)
print(id(b3))