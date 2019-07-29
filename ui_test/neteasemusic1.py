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
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('http://music.163.com/#/discover/toplist?id=60198')
# 切入到frame
driver.switch_to.frame("contentFrame")
div = driver.find_element_by_id("song-list-pre-cache")
print(div.text)

# 切回到默认frame
driver.switch_to.default_content()



driver.quit()