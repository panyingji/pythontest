# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : user.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-07-15 18:25:34
 @ desc       : 
***********************************************
"""
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("Your fistName is %s,lastName is %s" % (self.first_name,self.last_name))

    def greet_user(self):
        print("Hi,%s %s,Welcome to my company!" % (self.first_name,self.last_name))

user1 = User("Pan","YingJi")
user2 = User("Ni","Lin")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

