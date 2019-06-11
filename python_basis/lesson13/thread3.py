import time
import threading


def do_something(something):
    for i in range(5):
        time.sleep(1)
        print(something)


def create_thread():
    global t2
    t2 = threading.Thread(target=do_something, args=["听音乐"])
    t2.start()


t1 = threading.Thread(target=create_thread)
t1.start()

print(t1.getName())
print(t2.getName())