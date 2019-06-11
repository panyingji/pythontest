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

# 捕获一种已知异常
# while True:
#     num = input('input a number:')
#     try:
#         print('100 / {} = {}'.format(num,100.0/int(num)))
#     except ZeroDivisionError as e:
#         print('除数不能为0！',e)




# 捕获多种已知异常
# while True:
#     num = input('input a number:')
#     try:
#         print('100 / {} = {}'.format(num,100.0/int(num)))
#     except ZeroDivisionError as e:
#         print('除数不能为0！',e)
#     except ValueError as e:
#         print('应该输入数值！',e)

# 捕获所有异常（已知/未知）
# while True:
#     num = input('input a number:')
#     try:
#         print('100 / {} = {}'.format(num, 100.0 / int(num)))
#     except ZeroDivisionError as e:
#         print('除数不能为0！', e)
#     except Exception as e:  # 所有异常的父类
#         print('有其他异常', e)




# 如果要知道异常信息
import traceback
while True:
    num = input('input a number:')
    try:
        print('100 / {} = {}'.format(num, 100.0 / int(num)))
    except:
        print('有异常！',traceback.format_exc())


# 不管是否有异常，都要执行一段代码，finall 一定要放在最后写
# while True:
#     num = input('input a number:')
#     try:
#         print('100 / {} = {}'.format(num, 100.0 / int(num)))
#     except ZeroDivisionError as e:
#         print('除数不能为0！', e)
#     except Exception as e:  # 所有异常的父类
#         print('有其他异常', e)
#     finally:
#         print('Done!')





# else语句，没有异常的情况下，要执行一段代码，else必须跟在所有的except后面，但在finally前面
# while True:
#     num = input('input a number:')
#     try:
#         print('100 / {} = {}'.format(num, 100.0 / int(num)))
#     except ZeroDivisionError as e:
#         print('除数不能为0！', e)
#     except Exception as e:  # 所有异常的父类
#         print('有其他异常', e)
#     else:
#         print('没有异常，也执行这段代码！')
#     finally:
#         print('Done!')


# 自定义异常，需要继承Exception父类，使用raise抛出异常
# class NameTooLongError(Exception):
#     err = 'name.long'
#
#     def methFun(self):
#         pass
#
#
# class NameTooShortError(Exception):
#     err = 'name.short'
#
#     def methFun(self):
#         pass
#
#
# # 使用raise抛出异常
# def inputName():
#     name = input('请输入5个字符的用户名：')
#     if len(name) > 5:
#         raise NameTooLongError
#     elif len(name) < 5:
#         raise NameTooShortError
#
#
# # 使用try...except捕获异常
# try:
#     inputName()
# except NameTooLongError:
#     print('名字太长！')
# except NameTooShortError:
#     print('名字太短！')


# 人为抛出异常
# for one in range(1, 6):
#     if one == 3:
#         raise ValueError
#     print(one)


# 断言异常
tel = input('输入手机号：')
assert len(tel) == 11,'手机号位数有误！'
print('我正在处理手机运营商操作')