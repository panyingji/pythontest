# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : apiLib.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-23 15:06:05
 @ desc       : 请求库
***********************************************
"""
import requests
from eduapi_project.config.config import *
import passwd_encrypt
from pprint import pprint

g_token = None

# 系统登录
def login(username,password,corpId,loginType=0,loginIdentityList=[0,1],captcha=""):
    '''
    :param username: 用户名
    :param password: 密码
    :param loginType: 登录类型（整型），0表示用户密码登录,1表示手机验证码登录,2表示声纹登陆,3表示人脸登陆
    :param corpId: 学校代码（字符串）
    :param loginIdentityList: 限定只能使用什么身份登陆，0:老师,1:学生,2:家长,3:平台管理员，
    因为老师和学生是同一个app，家长又是另外一个app,传参格式为一个列表，如：[0,1]
    :return:
    '''
    global g_token
    pwd = passwd_encrypt.passwdencry(password)
    body = {
        "username":username,
        "password":pwd,
        "corpId":corpId,
        "loginType":loginType,
        "loginIdentityList":loginIdentityList,
        "captcha":captcha
    }
    res = requests.post(f"http://{API_SERVER}/user/app/usercenter/login",json=body)
    retObj = res.json()
    try:
        g_token = retObj["body"]["token"]
    except:
        print("登录异常 ！")
    pprint(retObj)
    return retObj

# 获取个人信息
def getPersonDetail():
    res = requests.get(f"http://{API_SERVER}/user/app/usercenter/getPersonDetail",headers={"token":g_token})
    retObj = res.json()
    pprint(retObj)
    return retObj

