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

from random import randint
import time


class Tiger:  # 老虎类
    className = '老虎'  # 静态属性

    def __init__(self, inweight):  # 初始化方法-----对于实例而言-self形参---只要创建实例就会被自动调用
        # self为实例本身，创建实例时，会自动调用初始化方法，同时实例t1作为实参传给self，self语法上支持改成其他字符串，但不规范，不建议改
        self.weight = inweight  # 实例属性不能用 类.属性 的方式调用
        print('我是Tiger类的初始化方法')

    # 实例方法，针对具体的某个实例，每一个实例都不同
    def roar(self):
        print('我是老虎，我叫了！--体重减5斤')
        self.weight -= 5

    # 实例方法，针对具体的某个实例，每一个实例都不同
    def feed(self, food):
        if food == '肉':
            self.weight += 10
            print('喂食正确！')
        else:
            self.weight -= 10
            print('喂食错误！')

    # 静态方法定义，需要加 "@staticmethod"装饰器进行装饰，只能装饰当前方法
    @staticmethod
    def static_roar():
        print('wow!!!')


class Sheep:
    pass


t1 = Tiger(100)


# t1.roar()
# t1.feed('草')
# t1.static_roar()
# print(t1.weight)
# t2 = Tiger(200)
# print(t2.weight)

# 对象组合
class Room:
    def __init__(self, inNum, inAnimal):
        self.num = inNum
        self.animal = inAnimal


roomList = []
for one in range(1, 11):
    if randint(0, 1) == 1:
        ani = Tiger(200)
    else:
        ani = Sheep(100)
    room = Room(one, ani)
    roomList.append(room)

startTime = time.time()
while True:
    curTime = time.time()
    if curTime - startTime > 180:
        break

print(time.time())  # 单位为s，从1970年---至今

# 继承----单继承---java是串行继承，python不仅支持串行继承，还支持并行继承（多继承）
# class SouthTiger(Tiger):
#     pass
#
#
# s1 = SouthTiger()
# print(s1.className)


# 并行继承
# class SouthTiger(Tiger,Sheep):
#     pass