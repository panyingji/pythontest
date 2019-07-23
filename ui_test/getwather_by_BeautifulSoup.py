# -*- coding:utf-8 -*-
"""
***********************************************
 @ Project    : myproject
 @ FileName   : getwather_by_tag.py
 @ Author     : LEONE
 @ IDE        : PyCharm
 @ CreateTime : 2019-07-23 16:57:40
 @ Desc       : 
***********************************************
"""
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
ele = driver.find_element_by_id('forecastID')
print(ele)

html_doc = ele.get_attribute('innerHTML')
soup = BeautifulSoup(html_doc,'html5lib')
dls = soup.find_all('dl')

citys = []
for dl in dls:
    name = dl.dt.a.string
    ltemp = dl.dd.span.string
    ltemp = int(ltemp.replace('℃',''))
    print(name,ltemp)
    citys.append([name,ltemp])

lowest = None
lowestCitys = []
for one in citys:
    curcity = one[0]
    ltemp = one[1]
    if lowest == None or ltemp < lowest:
        lowest = ltemp
        lowestCitys = [curcity]
    elif ltemp == lowest:
        lowestCitys.append(curcity)
print('温度最低为%s℃，城市有%s' % (lowest,' '.join(lowestCitys)))

driver.quit()