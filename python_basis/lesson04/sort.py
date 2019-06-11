# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : sort.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       :
***********************************************
"""

aList = [7,2,5,9,3,8,4]
for i in range(0,len(aList)-1):
    for j in range(0,len(aList)-i-1):
        if aList[j] > aList[j+1]:
            aList[j],aList[j+1] = aList[j+1],aList[j]
print(aList)

bList = [7,2,5,9,3,8,4]
