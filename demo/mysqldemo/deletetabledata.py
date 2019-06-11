# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : deletetabledata.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-23 10:20:24
 @ desc       : 
***********************************************
"""
import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "TESTDB", charset='utf8' )
# 使用 cursor()方法获取操作游标
cursor = db.cursor()
# SQL 删除语句
sql = "delete from student where studentName = 'haha'"
try:
    # 执行 SQL 语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
    # 关闭连接
db.close()