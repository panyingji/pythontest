# -*- coding:utf-8 -*-
"""
***********************************************
 @ Project    : myproject
 @ FileName   : homework12306.py
 @ Author     : LEONE
 @ IDE        : PyCharm
 @ CreateTime : 2019-07-29 17:43:16
 @ Desc       : 
***********************************************
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
driver.maximize_window()
driver.implicitly_wait(10)
fromEle = driver.find_element_by_id('fromStationText')
fromEle.click()
fromEle.send_keys('南京南\n')
toEle = driver.find_element_by_id('toStationText')
toEle.click()
toEle.send_keys('杭州东\n')
Select(driver.find_element_by_id('cc_start_time')).select_by_visible_text('06:00--12:00')
driver.find_element_by_css_selector('#date_range ul li:nth-child(2)').click()
trains = driver.find_elements_by_xpath("//*[@id='queryLeftTable']/tr/td[4][@class]/../td[1]//a")
for one in trains:
    print(one.text)
input()
driver.quit()