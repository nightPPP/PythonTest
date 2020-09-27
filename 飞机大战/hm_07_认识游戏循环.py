import pygame

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
screen.blit(hero, (200, 500))

# 完成所有绘制，统一调用update
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

i = 0
# 游戏循环----意味着游戏真正要开始了
while True:
    clock.tick(60)
    print(i)

pygame.quit()