# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : test.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       :
***********************************************
"""

import requests
import pprint
import random
import datetime

# Server = '192.168.1.100'
Server = 'localhost'

g_sessionid = None
def login(username,password):
    global g_sessionid
    body = {
        "username":username,
        "password":password
    }
    res = requests.post(f'http://{Server}/api/mgr/loginReq', data=body)
    g_sessionid = res.cookies["sessionid"]
    print(f"sessionid:{g_sessionid}")
    retObj = res.json()
    # pprint.pprint(retObj)
    return retObj


def Get_Course():
    get_course = requests.get(f'http://{Server}/api/mgr/sq_mgr/', params={
        "action": "list_course",
        "pagenum": 1,
        "pagesize": 100
    },cookies={"sessionid":g_sessionid})
    pprint.pprint(get_course.json())
    return get_course.json()


# data格式创建课程
def Add_Course():
    '''
    data格式创建课程
    '''
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    num = str(random.randint(1, 100))
    courseName = 'python' + "_" + num + "_" + now  # 课程名称不重复
    add_course = requests.post(f'http://{Server}/api/mgr/sq_mgr/', data={
        "action": "add_course",
        "data": '''
                {{
                  "name":"{}",
                  "desc":"python语言",
                  "display_idx":"1"
                }}
    
        '''.format(courseName)
    },cookies={"sessionid":g_sessionid})
    pprint.pprint(add_course.json())
    return add_course.json()


def Add_Course1():
    '''
    课程名称不重复
    '''
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    num = str(random.randint(1, 100))
    courseName = 'python' + "_" + num + "_" + now  # 课程名称不重复
    add_course1 = requests.post(f'http://{Server}/api/mgr/sq_mgr/', data={
        "action": "add_course",
        "data": '''
                {
                  "name":"%s",
                  "desc":"python语言",
                  "display_idx":"1"
                }
    
        ''' % courseName
    },cookies={"sessionid":g_sessionid})
    pprint.pprint(add_course1.json())
    return add_course1.json()


# json格式创建课程
def Add_CourseJson():
    '''
    json格式创建课程
    '''
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    num = str(random.randint(1, 100))
    courseName = 'python' + "_" + num + "_" + now
    add_courseJson = requests.post(f'http://{Server}/apijson/mgr/sq_mgr/', json={
        "action": "add_course_json",
        "data": {
            "name": courseName,
            "desc": "python语言",
            "display_idx": "1"
        }
    },cookies={"sessionid":g_sessionid})
    pprint.pprint(add_courseJson.json())
    return add_courseJson.json()


def Modify_Add_Course():
    '''
    修改刚新增的课程信息
    '''
    add_courseid = Add_Course()["id"]
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    num = str(random.randint(1, 100))
    NewCourseName = 'python' + "_" + "Modify" + "_" + num + "_" + now  # 课程名称不重复
    modify_course = requests.put(f'http://{Server}/api/mgr/sq_mgr/', data={
        "action": "modify_course",
        "id": add_courseid,
        "newdata": '''
                {{
                  "name":"{}",
                  "desc":"初中化学课程",
                  "display_idx":"1"
                }}'''.format(NewCourseName)
    },cookies={"sessionid":g_sessionid})
    pprint.pprint(modify_course.json())

def Modify_Source_Course():
    '''
    在页面中随机修改一个课程名称
    '''
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    num = str(random.randint(1, 100))
    NewCourseName = 'python' + "_" + "ModifySourceCourse" + "_" + num + "_" + now  # 课程名称不重复
    idList = []
    RetList = Get_Course()["retlist"]
    if len(RetList) > 0:
        for one in RetList:
            idList.append(one["id"])
        index = random.randint(0, len(idList)-1)
        modify_course = requests.put(f'http://{Server}/api/mgr/sq_mgr/', data={
            "action": "modify_course",
            "id": idList[index],
            "newdata": '''
                            {{
                              "name":"{}",
                              "desc":"初中化学课程",
                              "display_idx":"1"
                            }}'''.format(NewCourseName)
        },cookies={"sessionid":g_sessionid})
        pprint.pprint(modify_course.json())
        return modify_course.json()
    else:
        print("数据为空！")



def Delete_Course():
    RetList = Get_Course()["retlist"]
    for one in RetList:
        if len(RetList) > 0:
            delete_course = requests.delete(f'http://{Server}/api/mgr/sq_mgr/', data={
                "action": "delete_course",
                "id": one["id"]
            },cookies={"sessionid":g_sessionid})
            pprint.pprint(delete_course.json())


# login("auto","sdfsdfsdf")
# Get_Course()
# Add_Course()
# Add_Course1()
# Add_CourseJson()
# Delete_Course()
# Get_Course()
# Modify_Add_Course()
# Modify_Source_Course()
# Get_Course()
