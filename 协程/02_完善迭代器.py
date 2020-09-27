import time


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_index = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.names):
            ret = self.names[self.current_index]
            self.current_index += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

for name in classmate:
    print(name)
    time.sleep(1)
