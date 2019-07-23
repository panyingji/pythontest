# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : test.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-06-26 16:41:07
 @ desc       : 
***********************************************
"""
import uiautomator2 as u2
import time


d = u2.connect('192.168.197.76')
d.unlock()
print(d.info)

d.app_start('com.pingan.educationHD')
# d(text="手机号登录").click()
d(resourceId='com.pingan.educationHD:id/et_crop').click()
d(resourceId='com.pingan.educationHD:id/et_crop').send_keys('K12测试学校(误删)壹')
d(text='K12测试学校(误删)壹').click()
d(resourceId="com.pingan.educationHD:id/et_username").send_keys('00027048')
d(resourceId="com.pingan.educationHD:id/et_password").send_keys('a1234567')
d.press("back")
d(resourceId="com.pingan.educationHD:id/tbtn_login").click()
d(resourceId="com.pingan.educationHD:id/iv_label_homework").click()
d.xpath('//*[@resource-id="com.pingan.educationHD:id/rv_latest_read"]/android.widget.RelativeLayout[1]').click()
d(resourceId="com.pingan.educationHD:id/tv_go_correct").click()
d.xpath('//*[@resource-id="root"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[7]/android.view.View[2]').click()
d(text="拍照上传答案").click()

# d(resourceId="com.pingan.educationHD:id/ll_icon").click()
# d(resourceId="com.pingan.educationHD:id/iv_logout").click()
# d(resourceId="com.pingan.educationHD:id/tv_positive").click()
time.sleep(5)
# d.app_stop('com.pingan.educationHD')