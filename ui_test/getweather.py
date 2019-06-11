# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : getweather.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-06-09 15:40:26
 @ desc       : 
***********************************************
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
res = driver.find_element_by_id('forecastID')
ret = res.text
print(ret)
citysWeather = res.text.split(u'℃\n')
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