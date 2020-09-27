import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "线程的名字是%s" %self.name
            print(msg)


if __name__ == "__main__":
    t = MyThread()
    t.start()