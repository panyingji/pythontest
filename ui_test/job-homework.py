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
driver.find_element_by_css_selector('.fltr a.more').click()
driver.find_element_by_id('work_position_input').click()
time.sleep(2)
citys = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em')
for city in citys:
    cityName = city.text
    selected = city.get_attribute('class')
    if (cityName == '深圳' and selected != 'on') or (cityName != '深圳' and selected == 'on'):
        city.click()
driver.find_element_by_id('work_position_click_bottom_save').click()
inputInfo = driver.find_element_by_css_selector('input#kwdselectid')
inputInfo.clear()
inputInfo.send_keys('Python')
time.sleep(1)
driver.find_element_by_css_selector('.tit').click()
driver.find_element_by_id('funtype_click').click()
time.sleep(1)
driver.find_element_by_css_selector('#funtype_click_center_right_list_category_0100_0100').click()
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
driver.find_element_by_id('funtype_click_bottom_save').click()
driver.find_element_by_css_selector('#cottype_list span.i_arrow').click()
driver.find_element_by_css_selector('.ul [title="民营公司"]').click()
driver.find_element_by_css_selector('#workyear_list .i_arrow').click()
driver.find_element_by_css_selector('.ul [title="1-3年"]').click()
driver.find_element_by_css_selector('.btnbox .p_but').click()
jobs = driver.find_elements_by_css_selector('#resultList div.el')
for job in jobs[1:]:
    fields = job.find_elements_by_tag_name('span')
    print('|'.join([field.text for field in fields]))
time.sleep(5)
input("Press any key to quit...")
driver.quit()


