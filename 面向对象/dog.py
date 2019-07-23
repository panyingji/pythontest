# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : dog.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-07-15 15:53:00
 @ desc       : 狗类
***********************************************
"""
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

my_dog = Dog("little",2)
my_dog2 = Dog("xiaohei",3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
print("My dog's name is " + my_dog2.name.title() + ".")
print("My dog is " + str(my_dog2.age) + " years old.")
print()
my_dog.sit()
my_dog.roll_over()
my_dog2.sit()
my_dog2.roll_over()
