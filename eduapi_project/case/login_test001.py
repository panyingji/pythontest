# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : login_test001.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-23 16:26:25
 @ desc       : 
***********************************************
"""
from eduapi_project.case.apiLib import *
import traceback,sys

retObjLogin = login("LEIJIE4522","a1234567","601878703267843")

SuccessCase001 = "【*******测试用例001执行通过*******】"
FailedCase001 = "【*******测试用例001执行失败*******】"


if retObjLogin["code"] == "200" and retObjLogin["message"] == "OK":
    try:
        assert retObjLogin["code"] == "200"
    except:
        print('登录检查点===>retObjLogin["code"] == "200"', traceback.format_exc())
        print(FailedCase001)
        sys.exit(1)
    try:
        assert retObjLogin["message"] == "OK"
    except:
        print('retObjLogin["message"] == "OK"', traceback.format_exc())
        print(FailedCase001)
        sys.exit(1)
    print("登录成功！")
    print(SuccessCase001)
elif retObjLogin["code"] == "300001001" and retObjLogin["message"] == "用户名或密码不正确":
    try:
        assert retObjLogin["code"] == "300001001"
    except:
        print('登录检查点===>retObjLogin["code"] == "300001001"', traceback.format_exc())
        print(FailedCase001)
        sys.exit(1)
    try:
        assert retObjLogin["message"] == "用户名或密码不正确"
    except:
        print('retObjLogin["message"] == "用户名或密码不正确"', traceback.format_exc())
        print(FailedCase001)
        sys.exit(1)
    print("登录失败！用户名或密码不正确")
    print(FailedCase001)
elif retObjLogin["code"] == "300001003" and retObjLogin["message"] == "图形验证码输入错误，请重新输入":
    try:
        assert retObjLogin["code"] == "300001003"
    except:
        print('登录检查点===>retObjLogin["code"] == "300001003"', traceback.format_exc())
        print(FailedCase001)
        sys.exit(1)
    try:
        assert retObjLogin["message"] == "图形验证码输入错误，请重新输入"
    except:
        print('retObjLogin["message"] == "图形验证码输入错误，请重新输入"', traceback.format_exc())
        print(FailedCase001)
        sys.exit(1)
    print("登录失败！图形验证码输入错误，请重新输入")
    print(FailedCase001)
elif retObjLogin["code"] == "300001065" and retObjLogin["message"] == "多次登录失败,请两分钟后重试":
    try:
        assert retObjLogin["code"] == "300001065"
    except:
        print('登录检查点===>retObjLogin["code"] == "300001065"', traceback.format_exc())
        print(FailedCase001)
        sys.exit(1)
    try:
        assert retObjLogin["message"] == "多次登录失败,请两分钟后重试"
    except:
        print('retObjLogin["message"] == "多次登录失败,请两分钟后重试"', traceback.format_exc())
        print(FailedCase001)
        sys.exit(1)
    print("登录失败！多次登录失败,请两分钟后重试")
    print(FailedCase001)
else:
    print("其他登录异常！")
    print(FailedCase001)



