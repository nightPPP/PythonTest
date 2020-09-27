import pygame

pygame.init()

# 创建游戏窗口---返回的是Surface
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 加载图像
bg = pygame.image.load("./images/background.png")
# blit绘制图形
screen.blit(bg, (0, 0))
# update更新
pygame.display.update()


while True:
    pass

pygame.quit()