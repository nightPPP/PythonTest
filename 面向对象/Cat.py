class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")

    def __init__(self):
        print("这是初始化方法")

# 当使用类名（）的时候，系统会做两件事
# 1，创建对象----为对象分配内存控件
# 2，初始化方法----为对象的属性设置初始值
tom = Cat()

tom.eat()
tom.drink()