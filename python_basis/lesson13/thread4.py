import time
import threading


def do_something(something):
    for i in range(5):
        print(f"CPU正在：{something}")
        time.sleep(1)


def bar(something):
    for i in range(15):
        print(f"CPU正在：{something}")
        time.sleep(1)


t1 = threading.Thread(target=do_something, args=['看书'])
t2 = threading.Thread(target=bar, args=['看电影'])


t1.start()
t2.start()
t1.join()     # 阻塞主线程,在start()方法调用之后调用,主线程需要等待子线程运行结束后才能退出
t2.join()

print(t1.getName())
print(t2.getName())