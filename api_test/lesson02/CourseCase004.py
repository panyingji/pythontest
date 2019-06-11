# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : CourseCase004.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       : 删除课程测试用例
***********************************************
"""

from lib.apiLib import *
import random, sys,traceback

login("auto", "sdfsdfsdf")

courseName = "Python_" + str(random.randint(0, 999999999))
SuccessCase004 = "【*******测试用例004执行通过*******】"
FailedCase004 = "【*******测试用例004执行失败*******】"

idList = []
ListBeforeDelte = listCourse("1", "9999999999")["retlist"]
if len(ListBeforeDelte) > 0:
    for one in ListBeforeDelte:
        idList.append(one["id"])
    index = random.randint(0, len(idList) - 1)
    print(f"下标为：{index}")
    print(f"被删除的课程id为:{idList[index]}")
    retObjDelete = deleteCourse(idList[index])
    if retObjDelete.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")

    ListAfterDelete = listCourse("1", "9999999999")["retlist"]
    if len(ListBeforeDelte) - len(ListAfterDelete) == 1:
        print("检查点===>课程数量，删除前比删除后课程数量多1，检查通过。")
    else:
        print("检查点===>课程数量，删除前比删除后课程数量不是多1，检查不通过！！！")
        print(f"\n{FailedCase004}\n")
    course = None
    for one in ListBeforeDelte:
        if one not in ListAfterDelete:
            course = one
            break

    try:
        assert course["id"] == idList[index]
    except:
        print('检查点错误：course["id"] == idList[index]',traceback.format_exc())
        print(f'{FailedCase004}')
        sys.exit(1)
    print(f"\n{SuccessCase004}\n")
else:
    print("=====页面列表数据为空，将调用新增课程接口创建课程以供删除=====")

    retObjAdd = addCourse(courseName, "人生苦短，我用Python", "1")
    ListAfterAdd = listCourse("1", "9999999999")["retlist"]
    AddCourseName = ListAfterAdd[0]["name"]
    print(f"新增用来修改的课程名称为：{AddCourseName}")
    print("====已调用新增课程接口创建课程====")
    DeleteId = retObjAdd["id"]
    retObjDelete = deleteCourse(DeleteId)
    ListAfterDelete = listCourse("1", "9999999999")["retlist"]
    if retObjDelete.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")
        print(f"\n{FailedCase004}\n")
    if len(ListAfterAdd) - len(ListAfterDelete) == 1:
        print("检查点===>课程数量，删除前比删除后课程数量多1，检查通过。")
    else:
        print("检查点===>课程数量，删除前比删除后课程数量不是多1，检查不通过！！！")
        print(f"\n{FailedCase004}\n")
    print(f"\n{SuccessCase004}\n")
