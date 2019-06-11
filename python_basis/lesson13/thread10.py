import threading,time

LockR = threading.RLock() # 定义递归锁


def foo1():
    LockR.acquire()
    print("A1锁")
    time.sleep(1)
    LockR.acquire()
    print("B1锁")
    LockR.release()
    print("B1锁释放")
    LockR.release()
    print("A1锁释放")


def foo2():
    LockR.acquire()
    print("B2锁")
    time.sleep(1)
    LockR.acquire()
    print("A2锁")
    LockR.release()
    print("A2锁释放")
    LockR.release()
    print("B2锁释放")


t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)

t1.start()
t2.start()