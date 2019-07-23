# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : restaurant.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-07-15 17:06:00
 @ desc       : 
***********************************************
"""
class Restaurant():
    """餐馆类"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("restauran's name is %s" % self.restaurant_name)
        print("restauran's type is %s" % self.cuisine_type)

    def open_restaurant(self):
        print("haha")

restaurant1 = Restaurant("zhangsan","555")
restaurant2 = Restaurant("lisi","666")
restaurant3 = Restaurant("wangwu","777")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
