import random
import pygame


# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PRE_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏--精灵"""

    def __init__(self, image_name, speed = 1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt = False):
        super().__init__("./images/background.png")
        # 是否是交替图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的方法实现
        super().update()
        # 判断是否移除屏幕,如果移除屏幕,将图像设置在屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")

        # 指定敌机的初始随机速度  1-3
        self.speed = random.randint(1, 3)

        # 指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)


    def update(self):
        # 调用父类方法，保持垂直方向的飞行
        super().update()

        # 判断是否飞出屏幕，如果是，需要从精灵组种删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出屏幕。。。")
            # kill()方法可以将精灵从所有的精灵组中移除，精灵就被自动销毁
            self.kill()

    def __del__(self):
        print("敌机销毁%s" % self.rect)