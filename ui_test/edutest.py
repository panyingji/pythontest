# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : edutest.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-06-09 20:07:57
 @ desc       : 
***********************************************
"""
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://edustg1.pingan.com/h5portal/onePortal/index.html#/login')
# driver.set_window_size(1950,1000)
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/form/div[1]/div/div/span/div/div/div/ul/li/div/input').send_keys(u'K12测试学校')
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="userName"]').send_keys('00026781')
driver.find_element_by_xpath('//*[@id="passWord"]').send_keys('a1234567')
ele = driver.find_element_by_xpath('//*[@id="loginBtn"]')
ele.click()

print(ele.get_attribute('outerHTML'))
print(ele.get_attribute('innerHTML'))
print(type(ele.get_attribute('outerHTML')))
print(type(ele.get_attribute('innerHTML')))



driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div[3]/span').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/span/div/div/div').click()
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[2]').click()
driver.find_element_by_css_selector('#content > div > div > div.ant-layout.ant-layout-has-sider > div.ant-layout-content > div > div > div > div > div.ant-tabs-bar > div > div > div > div > div:nth-child(4) > div').click()


driver.quit()