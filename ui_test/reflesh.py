# -*- coding:utf-8 -*-
"""
***********************************************
 @ Project    : myproject
 @ FileName   : reflesh.py
 @ Author     : LEONE
 @ IDE        : PyCharm
 @ CreateTime : 2019-07-29 17:38:55
 @ Desc       : 
***********************************************
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://check.ytesting.com')
driver.find_element_by_id('username').send_keys('sdfdsf')
driver.find_element_by_id('password').send_keys('sdfdsf')
time.sleep(2)
driver.refresh()
driver.forward()
driver.back()
time.sleep(5)
driver.quit()