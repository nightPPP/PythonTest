import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.current_index = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_index < len(self.obj.names):
            ret = self.obj.names[self.current_index]
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
