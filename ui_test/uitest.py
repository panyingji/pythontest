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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()



# 设置隐式等待（周期性检查元素是否出现，每隔半秒检查一次）
# driver.implicitly_wait(10)

driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('松勤')
driver.find_element_by_id('su').click()
# time.sleep(1)


# 设置显式等待
ele = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.ID,'1')))
# res = driver.find_element_by_id('1')
# res2 = res.text
print(ele.text)
if '松勤网 - 松勤软件测试' in ele.text:
    print('pass')
else:
    print('fail')
    print(ele.text)

time.sleep(3)


driver.quit()