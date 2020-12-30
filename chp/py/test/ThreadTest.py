#coding:utf8
# python 线程测试

import _thread
import time
import threading

# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s: %d" % ( threadName, time.ctime(time.time()), count), end="\n" )

def test1():
    try:
        _thread.start_new_thread(print_time, ("Thread-1", 2, ))
        _thread.start_new_thread(print_time, ("Thread-2", 4, ))
    except Exception as err:
        print("Error: 无法启动线程")

    while 1:
        pass


class myThread (threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadId
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程：", self.name)
        print_time(self.name, self.counter)
        print("退出线程：", self.name)

def test2():
    # 创建新线程
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # 开启新线程
    thread1.start()
    thread2.start()
    thread2.join()
    print("退出主线程")


def main():
    # test1()
    test2()

if __name__ == '__main__':
    main()