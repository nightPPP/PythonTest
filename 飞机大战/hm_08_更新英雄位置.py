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
screen.blit(hero, (150, 300))

# 完成所有绘制，统一调用update
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)
# 游戏循环----意味着游戏真正要开始了
while True:
    clock.tick(1)
    # 修改飞机的位置
    hero_rect.y -= 50

    # 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 调用update方法更新
    pygame.display.update()

pygame.quit()