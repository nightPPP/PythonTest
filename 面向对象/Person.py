class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字是 %s 我的体重是 %s 公斤" %(self.name, self.weight)

    def run(self):
        print("%s 爱跑步" %self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 吃东西" %self.name)
        self.weight += 1

person = Person("小明", 80)

person.run()
person.eat()

print(person)