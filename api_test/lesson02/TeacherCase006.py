# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : TeacherCase006.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       : 修改课程测试用例
***********************************************
"""

from lib.apiLib import *
import random, sys,traceback

login("auto", "sdfsdfsdf")

teacherName = "LEONE_" + str(random.randint(0, 999999999))
courseName = "Python_" + str(random.randint(0, 999999999))
teacherNameModify = "LEONE_" + "Modify_" + str(random.randint(0, 999999999))
teacherNameModifyRealName = "LEONE_" + "Modify_" + "RealName" + "_"+ str(random.randint(0, 999999999))

SuccessCase006 = "【*******测试用例006执行通过*******】"
FailedCase006 = "【*******测试用例006执行失败*******】"

TidList = []
TeacherListBeforeModify = listTeacher("1", "9999999999")["retlist"]
courseRetList = listCourse("1","999999999")["retlist"]
if len(courseRetList) > 0 and len(TeacherListBeforeModify) > 0:
    for one in TeacherListBeforeModify:
        TidList.append(one["id"])
    index_t = random.randint(0, len(TidList) - 1)
    print(f"下标为：{index_t}")
    print(f"将被修改的老师id为:{TidList[index_t]}")
    courseIdList = []
    courseNameList = []
    for course in courseRetList:
        courseIdList.append(course["id"])
        courseNameList.append(course["name"])
    index_c = random.randint(0,len(courseIdList) - 1)
    retObjModify = modifyTeacher(TidList[index_t], teacherNameModify,"a1234567",teacherNameModifyRealName,"老师名称修改操作！",
                                 [{"id":courseIdList[index_c],"name":courseNameList[index_c]}],"1")
    if retObjModify.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")
        print(f"\n{FailedCase006}\n")

    TeacherListAfterModify = listTeacher("1", "9999999999")["retlist"]

    if len(TeacherListBeforeModify) == len(TeacherListAfterModify):
        print("检查点===>老师数量，修改前和修改后老师数量相等，检查通过。")
    else:
        print("检查点===>老师数量，修改前和修改后老师数量不相等，检查不通过！！！")
        print(f"\n{FailedCase006}\n")
    teacher = None
    for one in TeacherListAfterModify:
        if one not in TeacherListBeforeModify:
            teacher = one
            break
    try:
        assert teacher["id"] == TidList[index_t]
    except:
        print('检查点错误：teacher["id"] == TidList[index_t]',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["username"] == teacherNameModify
    except:
        print('检查点错误：teacher["username"] == teacherNameModify',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["realname"] == teacherNameModifyRealName
    except:
        print('检查点错误：teacher["realname"] == teacherNameModifyRealName',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["desc"] == "老师名称修改操作！"
    except:
        print('检查点错误：teacher["desc"] == "老师名称修改操作！"',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["display_idx"] == 1
    except:
        print('检查点错误：teacher["display_idx"] == 1',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["courses"] == [{'course_id': courseIdList[index_c]}]
    except:
        print('检查点错误：teacher["courses"] == [{"course_id": courseIdList[index_c]}]',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    print(f"\n{SuccessCase006}\n")

elif len(courseRetList) == 0 and len(TeacherListBeforeModify) > 0:
    print("课程列表数据为空，需要先调用新增课程接口创建课程。")
    retObjAdd = addCourse(courseName, "人生苦短，我用Python", "1")
    courseList = listCourse("1", "9999999999")["retlist"]
    for one in TeacherListBeforeModify:
        TidList.append(one["id"])
    index_t = random.randint(0, len(TidList) - 1)
    print(f"下标为：{index_t}")
    print(f"将被修改的老师id为:{TidList[index_t]}")
    courseIdList = []
    courseNameList = []
    for course in courseList:
        courseIdList.append(course["id"])
        courseNameList.append(course["name"])
    index_c = random.randint(0,len(courseIdList) - 1)
    retObjModify = modifyTeacher(TidList[index_t], teacherNameModify,"a1234567",teacherNameModifyRealName,"老师名称修改操作！",
                                 [{"id":courseIdList[index_c],"name":courseNameList[index_c]}],"1")
    if retObjModify.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")
        print(f"\n{FailedCase006}\n")

    TeacherListAfterModify = listTeacher("1", "9999999999")["retlist"]

    if len(TeacherListBeforeModify) == len(TeacherListAfterModify):
        print("检查点===>老师数量，修改前和修改后老师数量相等，检查通过。")
    else:
        print("检查点===>老师数量，修改前和修改后老师数量不相等，检查不通过！！！")
        print(f"\n{FailedCase006}\n")
    teacher = None
    for one in TeacherListAfterModify:
        if one not in TeacherListBeforeModify:
            teacher = one
            break
    try:
        assert teacher["id"] == TidList[index_t]
    except:
        print('检查点错误：teacher["id"] == TidList[index_t]',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["username"] == teacherNameModify
    except:
        print('检查点错误：teacher["username"] == teacherNameModify',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["realname"] == teacherNameModifyRealName
    except:
        print('检查点错误：teacher["realname"] == teacherNameModifyRealName',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["desc"] == "老师名称修改操作！"
    except:
        print('检查点错误：teacher["desc"] == "老师名称修改操作！"',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["display_idx"] == 1
    except:
        print('检查点错误：teacher["display_idx"] == 1',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["courses"] == [{'course_id': courseIdList[index_c]}]
    except:
        print('检查点错误：teacher["courses"] == [{"course_id": courseIdList[index_c]}]',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    print(f"\n{SuccessCase006}\n")

elif len(courseRetList) > 0 and len(TeacherListBeforeModify) == 0:
    print("老师列表数据为空，需要先调用新增老师接口创建老师。")
    ListBeforeAdd = listCourse("1", "9999999999")["retlist"]
    courseIdList = []
    courseNameList = []
    for course in courseRetList:
        courseIdList.append(course["id"])
        courseNameList.append(course["name"])
    index_c = random.randint(0, len(courseIdList) - 1)
    retObjAdd = addTeacher(teacherName,"a1234567","潘英基","语文老师",
                           [{"id":courseIdList[index_c],"name":courseNameList[index_c]}],"1")
    TeacherListBeforeModify_1 = listTeacher("1","999999999")["retlist"]
    ModifyTeacherId = retObjAdd["id"]
    retObjModify = modifyTeacher(ModifyTeacherId, teacherNameModify,"a1234567",teacherNameModifyRealName,"老师名称修改操作！",
                                 [{"id":courseIdList[index_c],"name":courseNameList[index_c]}],"1")
    TeacherListAfterModify = listTeacher("1","999999999")["retlist"]
    if retObjModify.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")
        print(f"\n{FailedCase006}\n")

    if len(TeacherListBeforeModify_1) == len(TeacherListAfterModify):
        print("检查点===>老师数量，修改前和修改后老师数量相等，检查通过。")
    else:
        print("检查点===>老师数量，修改前和修改后老师数量不相等，检查不通过！！！")
        print(f"\n{FailedCase006}\n")
    teacher = None
    for one in TeacherListAfterModify:
        if one not in TeacherListBeforeModify_1:
            teacher = one
            break
    try:
        assert teacher["id"] == ModifyTeacherId
    except:
        print('检查点错误：teacher["id"] == ModifyTeacherId',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["username"] == teacherNameModify
    except:
        print('检查点错误：teacher["username"] == teacherNameModify',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["realname"] == teacherNameModifyRealName
    except:
        print('检查点错误：teacher["realname"] == teacherNameModifyRealName',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["desc"] == "老师名称修改操作！"
    except:
        print('检查点错误：teacher["desc"] == "老师名称修改操作！"',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["display_idx"] == 1
    except:
        print('检查点错误：teacher["display_idx"] == 1',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["courses"] == [{'course_id': courseIdList[index_c]}]
    except:
        print('检查点错误：teacher["courses"] == [{"course_id": courseIdList[index_c]}]',traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    print(f"\n{SuccessCase006}\n")

else:
    print("系统既不存在课程数据，也不存在老师数据 ！")
    print("将新增课程和老师数据 ！")
    # 新增课程及提取所新增课程的id及名称
    retObjAddCourseId = addCourse(courseName,"人生苦短，我用Python","1")["id"]
    addCourseList = listCourse("1","999999999")["retlist"]
    addCourseName = addCourseList[0]["name"]

    # 新增老师并拿到老师id
    retObjAddTeacherId = addTeacher(teacherName,"a1234567","潘英基","Python老师",
                                    [{"id":retObjAddCourseId,"name":addCourseName}],"1")["id"]
    TeacherListBeforeModify_1 = listTeacher("1", "999999999")["retlist"]
    # 修改老师
    retObjAddTeacher = modifyTeacher(retObjAddTeacherId,teacherNameModify,"a1234567",teacherNameModifyRealName,"老师名称修改操作！",
                                     [{"id":retObjAddCourseId,"name":addCourseName}],"1")

    TeacherListAfterModify = listTeacher("1", "999999999")["retlist"]

    if retObjAddTeacher.get("retcode", None) == 0:
        print("检查点===>返回结果为0，检查通过。")
    else:
        print("检查点===>返回结果不为0，检查不通过！！！！")
        print(f"\n{FailedCase006}\n")

    if len(TeacherListBeforeModify_1) == len(TeacherListAfterModify):
        print("检查点===>老师数量，修改前和修改后老师数量相等，检查通过。")
    else:
        print("检查点===>老师数量，修改前和修改后老师数量不相等，检查不通过！！！")
        print(f"\n{FailedCase006}\n")
    teacher = None
    for one in TeacherListAfterModify:
        if one not in TeacherListBeforeModify_1:
            teacher = one
            break
    try:
        assert teacher["id"] == retObjAddTeacherId
    except:
        print('检查点错误：teacher["id"] == retObjAddTeacherId', traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["username"] == teacherNameModify
    except:
        print('检查点错误：teacher["username"] == teacherNameModify', traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["realname"] == teacherNameModifyRealName
    except:
        print('检查点错误：teacher["realname"] == teacherNameModifyRealName', traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["desc"] == "老师名称修改操作！"
    except:
        print('检查点错误：teacher["desc"] == "老师名称修改操作！"', traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["display_idx"] == 1
    except:
        print('检查点错误：teacher["display_idx"] == 1', traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    try:
        assert teacher["courses"] == [{'course_id': retObjAddCourseId}]
    except:
        print('检查点错误：teacher["courses"] == [{"course_id": retObjAddCourseId}]', traceback.format_exc())
        print(f'{FailedCase006}')
        sys.exit(1)
    print(f"\n{SuccessCase006}\n")