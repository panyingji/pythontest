# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : CourseCase001.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       : 新增课程测试用例
***********************************************
"""

from lib.apiLib import *
import random, sys,traceback

login("auto", "sdfsdfsdf")

SuccessCase001 = "【*******测试用例001执行通过*******】"
FailedCase001 = "【*******测试用例001执行失败*******】"

courseName = "Python_" + str(random.randint(0, 999999999))
retObBefore = listCourse("1", "9999999999")["retlist"]
retObjAdd = addCourse(courseName, "人生苦短，我用Python", "1")

if retObjAdd.get("retcode", None) == 0:
    print("检查点===>返回结果为0，检查通过。")
else:
    print("检查点===>返回结果不为0，检查不通过！！！！")

retObjAfter = listCourse("1", "9999999999")["retlist"]

if len(retObjAfter) - len(retObBefore) == 1:
    print("检查点===>添加课程之后，多出一门课程，检查通过。")
else:
    print("检查点===>添加课程之后，没有多出一门课程，检查不通过！！！！")

course = None
for one in retObjAfter:
    if one not in retObBefore:
        course = one
        break

try:
    assert course["name"] == courseName
except:
    print('检查点错误：course["name"] == courseName',traceback.format_exc())
    print(f'{FailedCase001}')
    sys.exit(1)
try:
    assert course["desc"] == "人生苦短，我用Python"
except:
    print('检查点错误：course["desc"] == "人生苦短，我用Python"',traceback.format_exc())
    print(f'{FailedCase001}')
    sys.exit(1)
try:
    assert course["display_idx"] == 1
except:
    print('检查点错误：course["display_idx"] == 1',traceback.format_exc())
    print(f'{FailedCase001}')
    sys.exit(1)
try:
    assert course["id"] == retObjAdd["id"]
except:
    print('检查点错误：course["id"] == retObjAdd["id"]',traceback.format_exc())
    print(f'{FailedCase001}')
    sys.exit(1)

print(f"\n{SuccessCase001}\n")
