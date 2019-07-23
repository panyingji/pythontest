# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : calculator.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-06-21 17:09:01
 @ desc       : 多多计算器
***********************************************
"""
from appium import webdriver
import traceback

desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.0",
    "deviceName": "testCalculator",
    "app": r'D:\apk\com.ibox.calculators_3.0.5_1305.apk',
    "appPackage": "com.ibox.calculators",
    "appActivity": "com.ibox.calculators.SplashActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": True,
    "newCommandTimeout": 6000
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

try:
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.ibox.calculators:id/digit3').click()
    driver.find_element_by_id('com.ibox.calculators:id/plus').click()
    driver.find_element_by_id('com.ibox.calculators:id/digit9').click()
    equal = driver.find_element_by_id('com.ibox.calculators:id/equal')
    equal.click()
    driver.find_element_by_id('com.ibox.calculators:id/mul').click()
    driver.find_element_by_id('com.ibox.calculators:id/digit5').click()
    equal.click()

    ele = driver.find_element_by_xpath("//*[@resource-id='com.ibox.calculators:id/activity_main_windows']//android.widget.RelativeLayout//android.widget.TextView[2]")
    print(ele.text)
    assert ele.text == '60' ,"测试不通过"

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()