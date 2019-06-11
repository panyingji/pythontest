# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : uitest.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-06-09 14:52:06
 @ desc       : 
***********************************************
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('松勤')
driver.find_element_by_id('su').click()
time.sleep(1)
res = driver.find_element_by_id('1')
res2 = res.text

if '松勤网 - 松勤软件测试' in res2:
    print('pass')
else:
    print('fail')
    print(res2)

time.sleep(5)


driver.quit()