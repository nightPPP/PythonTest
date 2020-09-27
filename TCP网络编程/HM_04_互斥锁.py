import threading
import time


glo_num = 0


def test1(num):

    global glo_num
    mutex.acquire()
    for i in range(num):
        glo_num += 1
    mutex.release()
    print("test1111----------%s" %str(glo_num))


def test2(num):
    global glo_num
    mutex.acquire()
    for i in range(num):
        glo_num += 1
    mutex.release()
    print("test2222----------%s" %str(glo_num))


# 创建互斥锁
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()