# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : apiLib.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       : 松勤VIP系统接口测试
***********************************************
"""

import requests
import pprint
import config
import json

# 登录系统
g_sessionid = None


def login(username, password):
    """
    :param username:
    :param password:
    :return:
    """
    global g_sessionid
    body = {
        "username": username,
        "password": password
    }
    res = requests.post(f'http://{config.API_SERVER}/api/mgr/loginReq', data=body)
    g_sessionid = res.cookies["sessionid"]
    print(f"sessionid:{g_sessionid}")
    retObj = res.json()
    pprint.pprint(retObj)
    return retObj


# 列出课程

def listCourse(pagenum="1", pagesize="20"):
    """
    :param pagenum:
    :param pagesize:
    :return:
    """
    res = requests.get(f'http://{config.API_SERVER}/api/mgr/sq_mgr/', params={
        "action": "list_course",
        "pagenum": pagenum,
        "pagesize": pagesize
    },
                       cookies={"sessionid": g_sessionid})
    retObj = res.json()
    pprint.pprint(retObj)
    return retObj


# 增加课程

def addCourse(name, desc, display_idx):
    res = requests.post(f'http://{config.API_SERVER}/api/mgr/sq_mgr/', data={
        "action": "add_course",
        "data": f'''
                    {{
                      "name":"{name}",
                      "desc":"{desc}",
                      "display_idx":"{display_idx}"
                    }}
                '''
    },
                        cookies={"sessionid": g_sessionid})
    retObj = res.json()
    pprint.pprint(retObj)
    return retObj


# 增加课程接口2

def addCourseJson(name, desc, display_idx):
    """
    :param name:
    :param desc:
    :param display_idx:
    :return:
    """
    res = requests.post(f'http://{config.API_SERVER}/apijson/mgr/sq_mgr/', json={
        "action": "add_course_json",
        "data": {
            "name": name,
            "desc": desc,
            "display_idx": display_idx
        }
    },
                        cookies={"sessionid": g_sessionid})
    retObj = res.json()
    pprint.pprint(retObj)
    return retObj


# 修改课程

def modifyCourse(courseid, name, desc, display_idx):
    """
    :param courseid:
    :param name:
    :param desc:
    :param display_idx:
    :return:
    """
    res = requests.put(f'http://{config.API_SERVER}/api/mgr/sq_mgr/', data={
        "action": "modify_course",
        "id": courseid,
        "newdata": f'''
                            {{
                              "name":"{name}",
                              "desc":"{desc}",
                              "display_idx":"{display_idx}"
                            }}'''
    }, cookies={"sessionid": g_sessionid})
    retObj = res.json()
    pprint.pprint(retObj)
    return retObj


# 删除课程

def deleteCourse(courseid):
    """
    :param courseid:
    :return:
    """
    res = requests.delete(f"http://{config.API_SERVER}/api/mgr/sq_mgr/", data={
        "action": "delete_course",
        "id": courseid
    },
                          cookies={"sessionid": g_sessionid})
    retObj = res.json()
    pprint.pprint(retObj)
    return retObj


# 列出老师

def listTeacher(pagenum,pagesize):
    """
    :param pagenum:
    :param pagesize:
    :return:
    """
    params = {
        "action":"list_teacher",
        "pagenum":pagenum,
        "pagesize":pagesize
    }
    res = requests.get(f'http://{config.API_SERVER}/api/mgr/sq_mgr/',params=params,cookies={"sessionid":g_sessionid})
    retObj = res.json()
    pprint.pprint(retObj)
    return retObj

# 增加老师
# courses参数格式为：[{"id":419,"name":"初中数学"},{"id":420,"name":"初中英语"}]
def addTeacher(username,password,realname,desc,courses,display_idx):
    """
    :param username:
    :param password:
    :param realname:
    :param desc:
    :param courses:
    :param display_idx:
    :return:
    """
    body = {
        "action":"add_teacher",
        "data":f'''
                {{
                    "username":"{username}",
                    "password":"{password}",
                    "realname":"{realname}",
                    "desc":"{desc}",
                    "courses":{json.dumps(courses)},
                    "display_idx":{display_idx}
                    
                }}
                '''
    }
    res = requests.post(f"http://{config.API_SERVER}/api/mgr/sq_mgr/",
                        data=body,
                        cookies={"sessionid":g_sessionid})
    retObj = res.json()
    pprint.pprint(retObj)
    return retObj

# 修改老师

# courses参数格式为：[{"id":419,"name":"初中数学"},{"id":420,"name":"初中英语"}]
def modifyTeacher(teacherid,username,password,realname,desc,courses,display_idx):
    """
    :param teacherid:
    :param username:
    :param password:
    :param realname:
    :param desc:
    :param courses:
    :param display_idx:
    :return:
    """
    body = {
        "action":"modify_teacher",
        "id":teacherid,
        "newdata":f"""
                    {{
                        "username":"{username}",
                        "password":"{password}",
                        "realname":"{realname}",
                        "desc":"{desc}",
                        "courses":{json.dumps(courses)},
                        "display_idx":{display_idx}
                    }}
                """
    }
    res = requests.put(f'http://{config.API_SERVER}/api/mgr/sq_mgr/',data=body,cookies={"sessionid":g_sessionid})
    retObj = res.json()
    pprint.pprint(retObj)
    return retObj

# 删除老师

def deleteTeacher(teacherid):
    body = {
        "action":"delete_teacher",
        "id":teacherid
    }
    res = requests.delete(f'http://{config.API_SERVER}/api/mgr/sq_mgr/',data=body,cookies={"sessionid":g_sessionid})
    retObj = res.json()
    print(retObj)
    return retObj


listCourse("1","20")
# modifyTeacher("238","LEONE","a1234567","潘英基","I am learning Python !",
#               [{"id":1455,"name":"python_80_2019-05-21 15:15:00"}],"1")
# deleteTeacher("238")
# addTeacher("LEONE1","a1234567","潘英基","潘英基老师",[{"id":"1455","name":"python_80_2019-05-21 15:15:00"}],"1")
# listTeacher("1","999999999")

# addCourse("python","python语言","1")