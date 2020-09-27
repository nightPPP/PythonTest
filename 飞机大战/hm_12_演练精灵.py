import pygame
from plane_sprites import *


pygame.init()

# 创建游戏窗口---返回的是Surface
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 加载图像
bg = pygame.image.load("./images/background.png")
# blit绘制图形
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# 完成所有绘制，统一调用update
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环----意味着游戏真正要开始了
while True:
    clock.tick(60)

    # 捕获事件
    # 监听事件
    for event in pygame.event.get():

        # 关闭按钮监听
        if event.type == pygame.QUIT:
            print("退出游戏。。。")
            pygame.quit()
            exit()

    # 修改飞机的位置
    hero_rect.y -= 1
    if hero_rect.y == 0:
        hero_rect.y = 700

    # 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法update和draw
    # 让所有的精灵更新位置
    enemy_group.update()
    # 在sreen上绘制所有的精灵
    enemy_group.draw(screen)

    # 调用update方法更新
    pygame.display.update()

pygame.quit()