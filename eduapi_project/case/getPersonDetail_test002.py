# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : getPersonDetail_test002.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-23 20:22:45
 @ desc       : 
***********************************************
"""
from eduapi_project.case.apiLib import *
import traceback,sys

retObjLogin = login("LEIJIE4522","a1234567","601878703267843")

SuccessCase002 = "【*******测试用例002执行通过*******】"
FailedCase002 = "【*******测试用例002执行失败*******】"

retObjDetail = getPersonDetail()

try:
    assert retObjDetail["code"] == "200"
except:
    print('登录检查点===>retObjLogin["code"] == "200"', traceback.format_exc())
    print(FailedCase002)
    sys.exit(1)
try:
    assert retObjDetail["message"] == "OK"
except:
    print('retObjLogin["message"] == "OK"', traceback.format_exc())
    print(FailedCase002)
    sys.exit(1)
print(SuccessCase002)