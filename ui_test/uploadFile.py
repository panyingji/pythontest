# -*- coding:utf-8 -*-
"""
***********************************************
 @ Project    : myproject
 @ FileName   : uploadFile.py
 @ Author     : LEONE
 @ IDE        : PyCharm
 @ CreateTime : 2019-07-29 16:51:24
 @ Desc       : 
***********************************************
"""
from selenium import webdriver
import win32com.client
import time

driver = webdriver.Chrome()
driver.get('https://tinypng.com')
driver.maximize_window()
driver.implicitly_wait(60)
print(driver.title)
driver.find_element_by_css_selector('figure.icon').click()
time.sleep(3)

shell = win32com.client.Dispatch("WScript.Shell")
# 有的系统要加 '\r'
# 有的系统要加 '\r\n'
shell.Sendkeys(r'D:\Python_Project\myproject\ui_test\pictures\uploadFileTest.png' + '\r\n')
input("...")
driver.quit()