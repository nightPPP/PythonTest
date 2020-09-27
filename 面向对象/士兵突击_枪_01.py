class Gun:

    def __init__(self, model):
        # 1，枪的型号
        self.model = model

        # 2，子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1，判断子弹的数量
        if self.bullet_count<=0:
            print("[%s]没有子弹了..."%self.model)
            return
        # 2，发射子弹
        self.bullet_count -= 1

        # 3，提示发射信息
        print("[%s]突突突...[%d]"%(self.model, self.bullet_count))

class Solders:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        # if self.gun == None:
        if self.gun is None:
            print("[%s]还没有枪。。。"%self.name)
            return

        print("冲啊。。。【%s】"%self.name)

        self.gun.add_bullet(50)
        self.gun.shoot()

ak47 = Gun("AK47")

xusanduo = Solders("许三多")
xusanduo.gun = ak47
xusanduo.fire()

print(xusanduo.gun)