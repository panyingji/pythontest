# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : TeacherCase007.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-23 11:04:53
 @ desc       : 删除老师测试用例
***********************************************
"""
from lib.apiLib import *
import random, sys,traceback

login("auto", "sdfsdfsdf")

teacherName = "LEONE_" + str(random.randint(0, 999999999))
SuccessCase007 = "【*******测试用例007执行通过*******】"
FailedCase007 = "【*******测试用例007执行失败*******】"

idList = []
ListBeforeDelete = listTeacher("1", "9999999999")["retlist"]
ListCourse = listCourse("1","999999999")["retlist"]
if len(ListBeforeDelete) > 0 and len(ListCourse) > 0:
    for one in ListBeforeDelete:
        idList.append(one["id"])
    index = random.randint(0, len(idList) - 1)
    print(f"下标为：{index}")
    print(f"被删除的课程id为:{idList[index]}")
    retObjDelete = deleteTeacher(idList[index])
    if retObjDelete.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")

    ListAfterDelete = listTeacher("1", "9999999999")["retlist"]
    if len(ListBeforeDelete) - len(ListAfterDelete) == 1:
        print("检查点===>老师数量，删除前比删除后老师数量多1，检查通过。")
    else:
        print("检查点===>老师数量，删除前比删除后老师数量不是多1，检查不通过！！！")
        print(f"\n{FailedCase007}\n")
    teacher = None
    for one in ListBeforeDelete:
        if one not in ListAfterDelete:
            teacher = one
            break
    try:
        assert teacher["id"] == idList[index]
    except:
        print('检查点错误：course["id"] == idList[index]',traceback.format_exc())
        print(f'{FailedCase007}')
        sys.exit(1)
    print(f"\n{SuccessCase007}\n")

elif len(ListCourse) == 0 and len(ListBeforeDelete) > 0:
    print("=====课程列表为空，老师列表非空,随机删除老师=====")
    ListBeforeDelete = listTeacher("1", "9999999999")["retlist"]
    teacherIdList = []
    for one in ListBeforeDelete:
        teacherIdList.append(one["id"])
    index_t = random.randint(0,len(teacherIdList) - 1)

    retObjDelete = deleteTeacher(teacherIdList[index_t])
    ListAfterDelete = listCourse("1", "9999999999")["retlist"]

    if retObjDelete.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")
        print(f"\n{FailedCase007}\n")
    if len(ListBeforeDelete) - len(ListAfterDelete) == 1:
        print("检查点===>课程数量，删除前比删除后老师数量多1，检查通过。")
    else:
        print("检查点===>课程数量，删除前比删除后老师数量不是多1，检查不通过！！！")
        print(f"\n{FailedCase007}\n")
    print(f"\n{SuccessCase007}\n")
elif len(ListCourse) > 0 and len(ListBeforeDelete) == 0:
    ListCourse = listCourse("1","999999999")["retlist"]
    index_c = 0
    courseId = []
    courseName = []
    for course in ListCourse:
        courseId.append(course["id"])
        courseName.append(course["name"])
    index_c = random.randint(0,len(courseId) - 1)
    teacherRealName = "LEONE_RealName" + "_" + str(random.randint(0, 999999999))
    retObjAdd = addTeacher(teacherName,"a1234567",teacherRealName,"Python老师操作 ！",
                       [{"id":courseId[index_c],"name":courseName[index_c]}],"1")
    DeleteId = retObjAdd["id"]
    ListBeforeDelete = listTeacher("1", "9999999999")["retlist"]
    retObjDelete = deleteTeacher(DeleteId)
    ListAfterDelete = listTeacher("1", "9999999999")["retlist"]
    if retObjDelete.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")
        print(f"\n{FailedCase007}\n")
    if len(ListBeforeDelete) - len(ListAfterDelete) == 1:
        print("检查点===>老师数量，删除前比删除后老师数量多1，检查通过。")
    else:
        print("检查点===>老师数量，删除前比删除后老师数量不是多1，检查不通过！！！")
        print(f"\n{FailedCase007}\n")
    print(f"\n{SuccessCase007}\n")
else:
    print("课程及老师数据为空 ！")
