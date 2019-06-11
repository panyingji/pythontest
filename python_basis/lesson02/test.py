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

print('hello\n'*3)
print('hello','tom')
print('hello','tom',sep='-')
print(round(100/3,6))

info = 'name is tom'
print(len(info))
print(info[0])              #第一个元素
print(info[len(info)-1])    #最后一个元素
print(info[-1])
print(info[-len(info)])     #负下标第一个元素
print(info[0 - len(info)])  #负下标第一个元素

#切片操作 [start:end:step]
print(info[5:5+2])          #切片左含右不含
print(info[:4])             #截取前半段
print(info[4:])
print(info[:-7])
print(info[-7:])
print(info[::-1])           #字符串翻转
print(info.index('n'))      #获取某字符的下标

#列表(序列类型)
aList = []                  #定义列表，列表中可存放任何类型的对象
name = 'tom'
bList = [10,3.14,'hello',[1,3,5],name]
print(type(aList))
print(len(bList))           #获取列表的元素个数
print(bList[-1])            #获取列表最后一个元素
print(bList[-1][-1])        #获取某个元素中的某个子元素
print(5 in bList)
print(bList[0:2])           #列表切出来仍然是列表，切片操作不改变类型
print(bList[3][:2])         #切子元素的元素

aList.append(200)           #在列表的尾部增加元素
print(aList)
aList.insert(1,300)         #insert[index,object]，在某个位置插入元素
print(aList)
aList.extend([400,500,600,700,800])     #合并列表
print(aList)
print(aList + [900,1000])    #临时操作，不保存到列表中
print(aList)
aList.reverse()
print('列表翻转：',aList)

#列表删除元素
del aList[-1]               #带下标删除，无返回值
print(aList)
del aList[0:2]              #删片段
print(aList)

res = aList.pop(0)          #带下标删除，返回被删除的元素
print('被删除的值为：',res)

aList.remove(500)           #找值进行删除，效率低下
print(aList)

#列表修改值
aList[0] = 1000
print('修改后的列表为：',aList)


#元组，可存储任何类型的对象，可进行切片操作（切出来后仍然为元组），但不可修改元素的个数和元素的值。
tu0 = (10)
print(type(tu0))
tu1 = (10,)                #只有一个元素时，需要加逗号
print(type(tu1))
tu2 = (10,3.14,'hello',[1,3,5])
print(tu2[0:1])            #结果为：(10,)

#元组的内置函数
tu3 = (1,2,3,3.14)
print(len(tu3))
print(max(tu3))            #元素不能含字符串/字符
print(min(tu3))            #元素不能含字符串/字符

tu4 = ('a','b','c')
print(max(tu4))            #元素不能含数字
print(min(tu4))            #元素不能含数字

#元组/列表相互转换
AList = [1,2,3,4]
Atu = (1,2,3,4,5)

Btu = tuple(AList)
print(Btu)
Blist = list(Atu)
print(Blist)