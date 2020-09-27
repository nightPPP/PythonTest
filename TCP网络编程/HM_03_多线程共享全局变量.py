import time
import threading


def sing(temp):
    temp.append(33)
    print("唱歌。。。%s" %str(temp))


def dance(sum):
    sum.append(44)
    print("跳舞。。。。。%s" %str(sum))


g_nums = [11, 22]


def main():
    t1 = threading.Thread(target=sing, args=(g_nums,))
    t2 = threading.Thread(target=dance, args=(g_nums,))
    t1.start()
    # time.sleep(1)
    t2.start()
    # time.sleep(1)


if __name__ == "__main__":
    main()
