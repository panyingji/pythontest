import time


def foo(something):
    for i in range(5):
        time.sleep(1)
        print(f"正在：{something}")


foo("看电影")
foo("听音乐")