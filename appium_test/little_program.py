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
import time

# 在微信任何地方输入：debugtbs.qq.com，点击debugtbs.qq.com，进入“tbs调试页面”，禁用掉“内核”

desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.0",
    "deviceName": "littleProgram",
    # "app": r'D:\apk\toutiao.apk',
    "appPackage": "com.tencent.mm",
    "appActivity": ".ui.LauncherUI",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": True,
    "newCommandTimeout": 6000
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(15)

size = driver.get_window_size()

driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("微信")')

x1 = size["width"] * 0.5
y1 = size["height"] * 0.3
y2 = size["height"] * 0.8

driver.swipe(x1,y1,x1,y2,2000)
time.sleep(2)

# 点击“星巴克”小程序

driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("星巴克用星说")').click()

# 下拉寻找“咖啡有你”

y2 = size["height"] * 0.5
# 一边下拉一边寻找元素
while 1:
    driver.swipe(x1,y2,x1,y2-600,1000)
    time.sleep(1)
    coffe = driver.find_element_by_xpath('//android.view.View[@text="咖啡有你"]')
    if coffe:
        driver.find_element_by_xpath('')
    break

input('**** Press to quit..')
driver.quit()