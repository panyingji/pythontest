import threading
import time

def do_something(something):
    for i in range(5):
        print("CPU 切换执行：",something)
        time.sleep(1)


# args通过列表或者元组进行传参数
# 并发：逻辑上具备同时处理多个任务的能力
# 并行：物理上在同一时刻执行多个并发任务
t1 = threading.Thread(target=do_something,args=["看电影"])
t2 = threading.Thread(target=do_something,args=("听音乐",))

if __name__ == '__main__':
    t1.start()
    t2.start()