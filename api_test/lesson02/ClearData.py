# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : ClearData.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 16:29:55
 @ desc       : 
***********************************************
"""
from lib.apiLib import *
import sys

# 删除所有课程数据

def clearCourse():
    courseList = listCourse("1","999999999")["retlist"]
    pprint.pprint(courseList)
    if len(courseList) > 0:
        for one in courseList:
            deleteCourse(one["id"])
        print("课程数据清空完毕！")
    else:
        print("课程数据为空，不执行清空课程程序，即将退出。")
        sys.exit(0)

# 删除所有老师数据

def clearTeacher():
    teacherList = listTeacher("1","99999999")["retlist"]
    if len(teacherList) > 0:
        for one in teacherList:
            deleteTeacher(one["id"])
        print("老师数据清空完毕！")
    else:
        print("老师数据为空，不执行清空老师程序，即将退出。")
        sys.exit(0)

clearCourse()
clearTeacher()