# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : mytoutiao.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-06-21 17:53:27
 @ desc       : 
***********************************************
"""
from appium import webdriver
import traceback

desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.0",
    "deviceName": "testTouTiao",
    "app": r'D:\apk\toutiao.apk',
    "appPackage": "io.manong.developerdaily",
    "appActivity": "io.toutiao.android.ui.activity.LaunchActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": True,
    "newCommandTimeout": 6000
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

try:
    # # 登录头条
    driver.implicitly_wait(10)
    driver.find_element_by_id('io.manong.developerdaily:id/tab_bar_plus').click()
    layOuts = driver.find_elements_by_class_name('android.widget.RelativeLayout')
    pwd = layOuts[1]
    pwd.click()
    driver.find_element_by_id('io.manong.developerdaily:id/edt_phone').send_keys('18607591131')
    driver.find_element_by_id('io.manong.developerdaily:id/edt_password').send_keys('199065')
    driver.find_element_by_id('io.manong.developerdaily:id/btn_login').click()

    # 退出头条
    # 操作元素“我的”
    driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("我的")').click()

    # 操作元素“设置”
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("io.manong.developerdaily:id/nav_btn_setting")').click()

    # 操作元素“退出当前账户”
    driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("退出当前账户")').click()

    # 操作弹窗元素“退出”
    driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("退出")').click()

except:
    print(traceback.format_exc())

driver.quit()