# -*- coding:utf-8 -*-
"""
***********************************************
 @ Project    : myproject
 @ FileName   : baidumusic.py
 @ Author     : LEONE
 @ IDE        : PyCharm
 @ CreateTime : 2019-07-24 15:11:03
 @ Desc       : 
***********************************************
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://music.taihe.com/top/new')
driver.find_element_by_id("__qianqian_pop_closebtn").click()
# div = driver.find_element_by_id("songListWrapper")
# liList = div.find_elements_by_tag_name('li')
liList = driver.find_elements_by_css_selector("#songListWrapper li")

for li in liList:
    upTags = li.find_elements_by_class_name('up')
    if upTags:
        # title = li.find_element_by_class_name("song-title ")
        # titleStr = title.find_element_by_tag_name("a").text
        titleStr = li.find_element_by_css_selector(".song-title  a").text
        authorsStr = li.find_element_by_class_name("author_list").text
        print(f'{titleStr:10s}:{authorsStr}')

driver.quit()
