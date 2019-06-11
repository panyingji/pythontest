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

# 字符串格式化输出
# 原始写法
name = 'Tom'
age = 30
print('名字是：%s，年龄是：%d' % (name, age))      # 多个元素，只能是元组，不能是列表！
print('名字是：%10s，年龄是：%10d' % (name, age))  # 指定宽度输出
print('名字是：%s，年龄是：%010d' % (name, age))   # 整形数字前面补0，%s不支持这种操作
print('名字是：%s，年龄是：%#X' % (name, age))     # “#” 在十六进制数字前面加上“0x”这样的前缀
print('%x' % 108)

print('%f' % 3.1415926)                           # %f 默认精确6位小数，并且做四舍五入操作
print('%.3f' % 3.14167)                           # %f 指定精度输出，并且做四舍五入操作
print('%6.3f' % 3.14167)                          # %6.3f 指定宽度输出，并且做四舍五入操作
print('%06.3f' % 3.14167)                         # %06.3f 指定宽度输出，并且做四舍五入操作，并且前面补0


# 牛逼的写法
# 顺序填坑
info = '名字是：{}，年龄是：{}'.format(name,age)           # 顺序填入法
info1 = '名字是：{}，年龄是：{}'.format(name,age,100)      # 可以多写
# info2 = '名字是：{}，年龄是：{}'.format(name)            # 不可以少写
info3 = '名字是：{:6}，年龄是：{:6}'.format(name,age)      # 指定宽度输出，字符串默认左对齐，数字默认右对齐
info4 = '名字是：{:>6}，年龄是：{:>6}'.format(name,age)    # 使用“<”，“>”来指定对齐方式
info5 = '名字是：{:$>6}，年龄是：{:#>6}'.format(name,age)  # 使用指定字符补齐
info6 = '名字是：{:$^6}，年龄是：{:#^6}'.format(name,age)  # 居中对齐
info11 = '名字是：{:$^6}，年龄是：{:#^6}'.format(name,age)
info12 = f'名字是：{name}，年龄是：{age}'                  # Python3.6以后才有的写法
info13 = f'名字是：{name:>6}，年龄是：{age:>6}'            # 也可以
info14 = '名字是：{:$^6}，年龄是：{:#^6}{{}}'.format(name,age)   #字符串中本来就有{}
print(info)
print(info1)
print(info3)
print(info4)
print(info5)
print(info6)
print(info12)
print(info13)
print(info14)

# 下标填坑
info7 = '名字是：{0}，年龄是：{1}'.format(name,age)
info8 = '名字是：{0:$>6}，年龄是：{1:#>6}'.format(name,age) # 指定宽度及补齐字符“#”
print(info7)
print(info8)

# 变量填坑
info9 = '名字是：{name}，年龄是：{age}'.format(name = 'Tom',age = 30)
print(info9)

# format处理浮点数
print('{}'.format(1234.567891234))
print('{:.2f}'.format(1234.567891234))
print('{:9.2f}'.format(1234.567891234))
print('{:09.2f}'.format(1234.567891234))
print('{:09.2f}{{}}'.format(1234.567891234))

# format处理十六进制数
print('{:x}'.format(108))
print('{:#6X}'.format(108))


# 文件路径的写法
'''
    1、路径的写法（3种）
        fileDir = 'G:/test.txt'
        fileDir = 'G:\\test.txt'
        fileDir = r'G:\test.txt'   #r 取消转义，推荐写法
'''