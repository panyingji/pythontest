# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : CourseCase002.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       : 校验同名课程测试用例
***********************************************
"""

from lib.apiLib import *
import random, sys,traceback

login("auto", "sdfsdfsdf")

SuccessCase002 = "【*******测试用例002执行通过*******】"
FailedCase002 = "【*******测试用例002执行失败*******】"

courseName = "Python_" + str(random.randint(0, 999999999))
retObjAddFirst = addCourse(courseName, "人生苦短，我用Python", "1")
retObListBefore = listCourse()["retlist"]

retObjAddSecond = addCourseJson(courseName, "人生苦短，我用Python", "1")

if retObjAddSecond.get("retcode", None) == 2:
    print("检查点===>返回结果为2，检查通过。")
else:
    print("检查点===>返回结果不为2，检查不通过！！！！")

if retObjAddSecond.get("reason", None) == "同名课程已经存在":
    print("检查点===>同名课程已经存在，检查通过。")
else:
    print("检查点===>同名课程已经存在，检查不通过！！！！")

retObjListAfter = listCourse()["retlist"]

try:
    assert retObListBefore == retObjListAfter
except:
    print("添加课程异常，课程名称没做唯一处理",traceback.format_exc())
    print(f"{FailedCase002}")
    sys.exit(1)

print(f"\n{SuccessCase002}\n")
