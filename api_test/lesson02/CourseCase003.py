# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : CourseCase003.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       : 修改课程测试用例
***********************************************
"""

from lib.apiLib import *
import random, sys,traceback

login("auto", "sdfsdfsdf")

courseName = "Python_" + str(random.randint(0, 999999999))
courseNameModify = "Python_" + "Modify_" + str(random.randint(0, 999999999))

SuccessCase003 = "【*******测试用例003执行通过*******】"
FailedCase003 = "【*******测试用例003执行失败*******】"

idList = []
ListBeforeModify = listCourse("1", "9999999999")["retlist"]
if len(ListBeforeModify) > 0:
    for one in ListBeforeModify:
        idList.append(one["id"])
    index = random.randint(0, len(idList) - 1)
    print(f"下标为：{index}")
    print(f"被修改的课程id为:{idList[index]}")
    retObjModify = modifyCourse(idList[index], courseNameModify, "人生苦短，我用Python", "1")
    if retObjModify.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")
        print(f"\n{FailedCase003}\n")

    ListAfterModify = listCourse("1", "9999999999")["retlist"]

    if len(ListBeforeModify) == len(ListAfterModify):
        print("检查点===>课程数量，修改前和修改后课程数量相等，检查通过。")
    else:
        print("检查点===>课程数量，修改前和修改后课程数量不相等，检查不通过！！！")
        print(f"\n{FailedCase003}\n")
    course = None
    for one in ListAfterModify:
        if one not in ListBeforeModify:
            course = one
            break

    try:
        assert course["id"] == idList[index]
    except:
        print('检查点错误：course["id"] == idList[index]',traceback.format_exc())
        print(f'{FailedCase003}')
        sys.exit(1)
    try:
        assert course["name"] == courseNameModify
    except:
        print('检查点错误：course["name"] == courseName',traceback.format_exc())
        print(f'{FailedCase003}')
        sys.exit(1)
    try:
        assert course["desc"] == "人生苦短，我用Python"
    except:
        print('检查点错误：course["desc"] == "人生苦短，我用Python"',traceback.format_exc())
        print(f'{FailedCase003}')
        sys.exit(1)
    try:
        assert course["display_idx"] == 2
    except:
        print('检查点错误：course["display_idx"] == 1',traceback.format_exc())
        print(f'{FailedCase003}')
        sys.exit(1)
    print(f"\n{SuccessCase003}\n")
else:
    print("页面列表数据为空，需要先调用新增课程接口创建课程。")
    retObjAdd = addCourse(courseName, "人生苦短，我用Python", "1")
    ListBeforeAdd = listCourse("1", "9999999999")["retlist"]
    AddCourseName = ListBeforeAdd[0]["name"]
    print(f"新增用来修改的课程名称为：{AddCourseName}")
    ModifyId = retObjAdd["id"]
    retObjModify = modifyCourse(ModifyId, courseNameModify, "人生苦短，我用Python", "1")
    if retObjModify.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")
        print(f"\n{FailedCase003}\n")

    ListAfterAdd = listCourse("1", "9999999999")["retlist"]

    if len(ListBeforeAdd) == len(ListAfterAdd):
        print("检查点===>课程数量，修改前和修改后课程数量相等，检查通过。")
    else:
        print("检查点===>课程数量，修改前和修改后课程数量不相等，检查不通过！！！")
        print(f"\n{FailedCase003}\n")
    course = None
    for one in ListAfterAdd:
        if one not in ListBeforeAdd:
            course = one
            break

    try:
        assert course["id"] == ModifyId
    except:
        print('检查点错误：course["id"] == ModifyId',traceback.format_exc())
        print(f'{FailedCase003}')
        sys.exit(1)
    try:
        assert course["name"] == courseNameModify
    except:
        print('检查点错误：course["name"] == courseName',traceback.format_exc())
        print(f'{FailedCase003}')
        sys.exit(1)
    try:
        assert course["desc"] == "人生苦短，我用Python"
    except:
        print('检查点错误：course["desc"] == "人生苦短，我用Python"',traceback.format_exc())
        print(f'{FailedCase003}')
        sys.exit(1)
    try:
        assert course["display_idx"] == 1
    except:
        print('检查点错误：course["display_idx"] == 1',traceback.format_exc())
        print(f'{FailedCase003}')
        sys.exit(1)
    print(f"\n{SuccessCase003}\n")