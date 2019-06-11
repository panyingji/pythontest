import threading,time

lockA = threading.Lock()
lockB = threading.Lock()


def foo1():
    lockA.acquire()
    print("A1锁")
    time.sleep(1)
    lockB.acquire()
    print("B1锁")
    lockB.release()
    print("B1锁释放")
    lockA.release()
    print("A1锁释放")


def foo2():
    lockB.acquire()
    print("B2锁")
    time.sleep(1)
    lockA.acquire()
    print("A2锁")
    lockA.release()
    print("A2锁释放")
    lockB.release()
    print("B2锁释放")


t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)

t1.start()
t2.start()