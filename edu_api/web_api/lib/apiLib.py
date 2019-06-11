# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : apiLib.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       : 智慧教育测试用例库
***********************************************
"""

import requests
import edu_config
from pprint import pprint
import passwd_encrypt

# 获取学校corpId

def schoolCoryid():
    payload = {
        "pageNum":"1",
        "pageSize":"50",
        "searchText":"K12"
    }
    res = requests.get(f'{edu_config.API_SERVER}/user/web/usercenter/getCorpList',json=payload)
    retObj = res.json()
    pprint(retObj)
    return retObj

# 登录系统

g_jsessionid = None    # JSESSIONID作为全局变量，为后续请求做准备
def login(username,password):
    global g_jsessionid  # 声明要使用该全局变量
    pwd = passwd_encrypt.passwdencry(password)
    payload = {
        "userName":username,
        "password":pwd,
        "corpId":"601878703267843", # 使用学校：K12测试学校(误删)壹
        "loginType":0,
        "loginIdentityList":[
            0,
            1
    ],
    "captcha":""
    }
    res = requests.post(f'{edu_config.API_SERVER}/user/web/usercenter/v2/login',json=payload)
    g_jsessionid = res.cookies["JSESSIONID"]
    print(g_jsessionid)
    retObj = res.json()
    pprint(retObj)

def testJsessionid():
    header = {
        "x-requested-with": "XMLHttpRequest",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "content-type": "application/json;charset=utf-8"
    }
    res = requests.get(f'{edu_config.API_SERVER}/homework/web/common/getChapterInfoBySource',params={
        "materialId":"743522429763594",
        "recentResource":"D"
    },
                       headers=header,
                       cookies={"JSESSIONID": g_jsessionid})
    retObj = res.json()
    pprint(retObj)

login("LIFUTE277","a1234567")
testJsessionid()