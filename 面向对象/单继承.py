class Animal(object):

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

class Dog(Animal):

    def bark(self):
        print("汪汪叫")


animal = Animal()
animal.eat()
animal.drink()
animal.run()
animal.sleep()

dog = Dog()
dog.bark()
dog.eat()