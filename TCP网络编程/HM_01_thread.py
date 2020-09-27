import time
import threading


def sing():
    for i in range(5):
        print("唱歌。。。")
        time.sleep(1)


def dance():
    for i in range(5):
        print("跳舞。。。。。")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    while True:
        lenght = len(threading.enumerate())
        print("当前运行的线程数为：%d" %lenght)
        if lenght <= 1:
            break

        time.sleep(0.5)


if __name__ == "__main__":
    main()