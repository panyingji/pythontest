# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : test_subprocess.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-25 13:10:22
 @ desc       :
***********************************************
"""
import subprocess
from subprocess import Popen,PIPE

# 1、check_output()只能获取标准输出（程序正常运行时），如果程序运行错误，则无法获取标准错误输出
# 2、也就是说，操作系统分为两种输出：标准输出 和 标准错误输出
# 3、check_output()需要等到被调用程序退出，才能返回
#ret = subprocess.check_output("ifconfig",shell=True,encoding='gbk')
#print(ret)
#print(ret.decode('gbk'))


# Popen为非阻塞性调用
#process = Popen(args='mspaint',shell=True)
#stdout,stderr = process.communicate()
#print("done")


popen = Popen(
    'dir E:dfasdsa',
    stdout = PIPE,
    stderr= PIPE,
    shell = True,
    #encoding='gbk'
)

output,err = popen.communicate()
print(type(output))
print(output)
print(err)
