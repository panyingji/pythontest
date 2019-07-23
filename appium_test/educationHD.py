# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : little_program.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-06-24 20:32:36
 @ desc       : 
***********************************************
"""
from appium import webdriver
import traceback

desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.0",
    "deviceName": "HuaWeiPad",
    "app": r"D:\apk\k12_pad_20190626100329_debug.apk",
    "appPackage": "com.pingan.educationHD",
    "appActivity": "com.pingan.education.portal.load.activity.LoadActivity",
    # "appWaitActivity": "com.pingan.education.portal.login.activity.LoginActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": True,
    "newCommandTimeout": 6000
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print(driver.contexts)
print(driver.current_context)
try:
    driver.implicitly_wait(10)
    # ele = driver.find_element_by_android_uiautomator('new UiSelector().textContains("手机号登录")')
    # ele.click()
    # driver.find_element_by_xpath('//android.widget.TextView[@text="手机号登录"]').click()
    # driver.find_element_by_android_uiautomator(
    #     'new UiSelector().className("android.widget.TextView").text("手机号登录")').click()
    # driver.find_element_by_android_uiautomator(
    #     'new UiSelector().className("android.widget.TextView").text("账号密码登录")').click()
    driver.find_element_by_xpath('//*[@text="手机号登录"]').click()
except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()

