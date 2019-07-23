# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : electric_car.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-07-16 10:40:43
 @ desc       : 
***********************************************
"""
import car

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self,battery_size=85):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)

class ElectricCar(car.Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        # self.battery_size = 70
        self.battery = Battery()

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

class TestSomething(ElectricCar):
    def test(self):
        self.read_odometer()
        super().fill_gas_tank()

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.fill_gas_tank()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
#
# print()
#
#
# from collections import OrderedDict
#
# favorite_languages = OrderedDict()
# favorite_languages['jen'] = 'python'
# favorite_languages['sarah'] = 'c'
# favorite_languages['edward'] = 'ruby'
# favorite_languages['phil'] = 'python'
#
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")
obj = TestSomething('a','b',100)
obj.test()
print(TestSomething.__mro__)