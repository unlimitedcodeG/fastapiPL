import pygame
import random

# 初始化Pygame
pygame.init()

# 设置窗口
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Songkran Splash")

# 设置颜色
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# 游戏变量
running = True
clock = pygame.time.Clock()
player_pos = [screen_width // 2, screen_height - 50]
player_speed = 5
score = 0
lives = 5

# 玩家和敌人列表
enemies = []
bullets = []

# 玩家和敌人尺寸
player_size = 50
enemy_size = 50
bullet_size = 10

# 时间控制
enemy_timer = 90
bullet_timer = 0

# 主游戏循环
while running:
    screen.fill(WHITE)  # 背景色

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 发射子弹
                bullets.append(
                    [player_pos[0] + player_size // 2 - bullet_size // 2, player_pos[1]]
                )

    # 玩家控制
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > player_speed:
        player_pos[0] -= player_speed
    if (
        keys[pygame.K_RIGHT]
        and player_pos[0] < screen_width - player_size - player_speed
    ):
        player_pos[0] += player_speed

    # 绘制玩家
    pygame.draw.rect(
        screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size)
    )

    # 敌人生成逻辑
    if enemy_timer <= 0:
        enemies.append([random.randint(0, screen_width - enemy_size), 0])
        enemy_timer = 90
    else:
        enemy_timer -= 1

    # 敌人移动和绘制
    for enemy in enemies[:]:
        enemy[1] += 2
        if enemy[1] > screen_height:
            enemies.remove(enemy)
            lives -= 1
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # 子弹移动和绘制
    for bullet in bullets[:]:
        bullet[1] -= 4
        if bullet[1] < 0:
            bullets.remove(bullet)
        pygame.draw.rect(screen, BLUE, (bullet[0], bullet[1], bullet_size, bullet_size))

    # 子弹和敌人碰撞检测
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (enemy[0] < bullet[0] < enemy[0] + enemy_size) and (
                enemy[1] < bullet[1] < enemy[1] + enemy_size
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # 更新屏幕显示
    pygame.display.flip()
    clock.tick(60)  # FPS

pygame.quit()
