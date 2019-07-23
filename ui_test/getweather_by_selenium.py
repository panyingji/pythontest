# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : getweather_by_selenium.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-06-09 15:40:26
 @ desc       : 
***********************************************
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
res = driver.find_element_by_id('forecastID')
ret = res.text
# print(ret)
citysWeather = res.text.split(u'℃\n')
# print(one for one in citysWeather)
# print([one for one in citysWeather])
print(type([one for one in citysWeather]))
print(id([one for one in citysWeather]))
print(type(citysWeather))
print(id(citysWeather))
for one in citysWeather:
    print(one)
print(citysWeather)
lowest = 100
lowestCity = []
for one in citysWeather:
    one = one.replace(u'℃','')
    print(one)
    curcity = one.split('\n')[0]
    lowweather = one.split('/')[1]
    lowweather = int(lowweather)
    if lowweather<lowest:
        lowest = lowweather
        lowestCity = [curcity]
    elif lowweather == lowest:
        lowestCity.append(curcity)
print('温度最低为%s℃, 城市有%s' % (lowest, ' '.join(lowestCity)))
driver.quit()