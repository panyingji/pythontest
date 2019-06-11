import time
import threading


# 守护线程
def foo(num):
    while True:
        time.sleep(0.1)
        print("听音乐",num)


t1 = threading.Thread(target=foo, args=[1])
t2 = threading.Thread(target=foo, args=[2])

"""
# 设置守护线程，必须在start()方法之前调用之前调用,主线程运行结束,其子线程一起结束
# 此时如果t2不设置守护线程，则主线程即使运行完print("电影结束")语句，也不会退出，
# 因为，t2还没结束，所以主线程不会退出，也就导致了t1不会退出。
"""
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()

# t1.setName("线程1")
# name = t1.getName()
# print(name)

# 主线程要做的事情
for i in range(20):
    time.sleep(0.1)
    print("看电影")
print("电影结束")

