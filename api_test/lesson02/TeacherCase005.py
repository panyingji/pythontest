# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : TeacherCase005.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 13:27:54
 @ desc       : 新增老师测试用例
***********************************************
"""
from lib.apiLib import *
import random, sys,traceback

login("auto", "sdfsdfsdf")

SuccessCase005 = "【*******测试用例005执行通过*******】"
FailedCase005 = "【*******测试用例005执行失败*******】"

courseName = "Python_" + str(random.randint(0, 999999999))
teacherName = "LEONE_" + str(random.randint(0, 999999999))
courseList = listCourse("1","999999999")["retlist"]

if len(courseList) == 0:
    # 增加老师之前，如果课程列表为空，则需要先增加一门课程
    print("系统不存在课程数据，将新增一门课程用来与老师绑定！")
    retObjb = addCourse(courseName,"人生苦短，我用Python ！","1")
    retObjCourseName = listCourse("1","999999999")["retlist"][0]["name"]
    print(retObjCourseName)
    teachCourseId_1 = retObjb["id"]
    retObBefore = listTeacher("1", "999999999")["retlist"]
    retObjAdd = addTeacher(teacherName, "a1234567", "潘英基", "语文老师",
                             [{"id": teachCourseId_1, "name": retObjCourseName}],"1")
    if retObjAdd.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")
    retObjAfter = listTeacher("1", "999999999")["retlist"]
    if len(retObjAfter) - len(retObBefore) == 1:
        print("检查点===>添加老师之后，多出一个老师，检查通过。")
    else:
        print("检查点===>添加老师之后，没有多出一个老师，检查不通过！！！！")

    teacher = None
    for one in retObjAfter:
        if one not in retObBefore:
            teacher = one
            break
    try:
        assert teacher["username"] == teacherName
    except:
        print('检查点错误：teacher["username"] == teacherName', traceback.format_exc())
        print(f'{FailedCase005}')
        sys.exit(1)
    try:
        assert teacher["desc"] == "语文老师"
    except:
        print('检查点错误：teacher["desc"] == "语文老师"', traceback.format_exc())
        print(f'{FailedCase005}')
        sys.exit(1)
    try:
        assert teacher["display_idx"] == 1
    except:
        print('检查点错误：teacher["display_idx"] == 1', traceback.format_exc())
        print(f'{FailedCase005}')
        sys.exit(1)
    try:
        assert teacher["id"] == retObjAdd["id"]
    except:
        print('检查点错误：teacher["id"] == retObjAdd["id"]', traceback.format_exc())
        print(f'{FailedCase005}')
        sys.exit(1)
else:
    # 系统已存在课程，则随机选取一门课程与老师绑定
    print("系统已存在课程，即将随机选取一门课程与老师绑定！")
    teachCourseIdList = []
    teachCourseNameList = []
    retObjList = listCourse("1","999999999")["retlist"]
    for one in retObjList:
        teachCourseIdList.append(one["id"])
        teachCourseNameList.append(one["name"])
    index = random.randint(0,len(teachCourseIdList) - 1)
    print(f"index:{index}")
    retObBefore = listTeacher("1","999999999")["retlist"]
    retObjAdd = addTeacher(teacherName,"a1234567","潘英基","语文老师",
                           [{"id":teachCourseIdList[index],"name":teachCourseNameList[index]}],"1")
    if retObjAdd.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")

    retObjAfter = listTeacher("1", "999999999")["retlist"]

    if len(retObjAfter) - len(retObBefore) == 1:
        print("检查点===>添加老师之后，多出一个老师，检查通过。")
    else:
        print("检查点===>添加老师之后，没有多出一个老师，检查不通过！！！！")

    teacher = None
    for one in retObjAfter:
        if one not in retObBefore:
            teacher = one
            break
    try:
        assert teacher["username"] == teacherName
    except:
        print('检查点错误：teacher["username"] == teacherName',traceback.format_exc())
        print(f'{FailedCase005}')
        sys.exit(1)
    try:
        assert teacher["desc"] == "语文老师"
    except:
        print('检查点错误：teacher["desc"] == "语文老师"',traceback.format_exc())
        print(f'{FailedCase005}')
        sys.exit(1)
    try:
        assert teacher["display_idx"] == 1
    except:
        print('检查点错误：teacher["display_idx"] == 1',traceback.format_exc())
        print(f'{FailedCase005}')
        sys.exit(1)
    try:
        assert teacher["id"] == retObjAdd["id"]
    except:
        print('检查点错误：teacher["id"] == retObjAdd["id"]',traceback.format_exc())
        print(f'{FailedCase005}')
        sys.exit(1)

print(f"\n{SuccessCase005}\n")