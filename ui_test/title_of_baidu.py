# -*- coding:utf-8 -*-
"""
***********************************************
 @ Project    : myproject
 @ FileName   : title_of_baidu.py
 @ Author     : LEONE
 @ IDE        : PyCharm
 @ CreateTime : 2019-07-29 15:02:07
 @ Desc       : 
***********************************************
"""
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.baidu.com')
print(driver.title)

driver.find_element_by_id('kw').send_keys('松勤')
driver.get_screenshot_as_file(r'D:\Python_Project\myproject\ui_test\pictures\shot.png')
time.sleep(1)
print(driver.title)
print(driver.current_url)
driver.quit()
