# -*- coding:utf-8 -*-
"""
***********************************************
 @ Project    : myproject
 @ FileName   : switchToFrame.py
 @ Author     : LEONE
 @ IDE        : PyCharm
 @ CreateTime : 2019-07-24 11:48:23
 @ Desc       : 
***********************************************
"""
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.w3school.com.cn/html/html_frames.asp')
driver.switch_to.alert.accept()