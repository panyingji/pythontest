# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : car.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-07-16 09:21:25
 @ desc       : 
***********************************************
"""


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100
        self.gas_tank = 200

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        """汽车油箱"""
        print("This car has a %s VL tank" % self.gas_tank)


# my_used_car = Car('subaru', 'outback', 2013)
# print( my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(-100)
# my_used_car.read_odometer()
