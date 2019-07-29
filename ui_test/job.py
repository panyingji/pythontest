# -*- coding:utf-8 -*-
"""
***********************************************
 @ Project    : myproject
 @ FileName   : job.py
 @ Author     : LEONE
 @ IDE        : PyCharm
 @ CreateTime : 2019-07-25 13:49:09
 @ Desc       : 
***********************************************
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.51job.com')
input1 = driver.find_element_by_id('kwdselectid')
input1.send_keys('Python')
# 获取输入框所输入的内容
value = input1.get_attribute('value')
print(value)
driver.find_element_by_id('work_position_input').click()
time.sleep(2)
citys = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em')
for city in citys:
    cityName = city.text
    selected = city.get_attribute('class')
    if (cityName == '杭州' and selected != 'on') or (cityName != '杭州' and selected == 'on'):
        city.click()
driver.find_element_by_id('work_position_click_bottom_save').click()
driver.find_element_by_css_selector('.ush button').click()
jobs = driver.find_elements_by_css_selector('#resultList div.el')
for job in jobs[1:]:
    fields = job.find_elements_by_tag_name('span')
    print('|'.join([field.text for field in fields]))
# driver.quit()