class Dog(object):

    @staticmethod
    def run():
        print("小狗在跑")


# dog = Dog()
# 不需要创建对象，类名+点调用
Dog.run()

