import sys
import pygame
import numpy as np

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,200)
GREEN = (0,200,0)
RED = (200,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("test test")

# 這裡提醒他們想一下哪些東西是屬於 block 的性質，把他們獨立出來
# ex: 這裡額外把 block_color 獨立出來了
# -----Block-----
block_center = (300,300)
block_width = 100
block_color = BLUE

rect = pygame.Rect(0,0,1,1)
rect.width = block_width
rect.height = block_width
rect.center = block_center
pygame.draw.rect(screen, block_color, rect)
# -----Block-----

# -----Ball-----
ball_center = np.array((40.0,200.0))
ball_v = np.array((6.0,3.0))
ball_radius = 20

def move_ball():
    global ball_center, ball_v
    ball_center = ball_center + ball_v
    ball_center = np.remainder(ball_center, [SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.draw.circle(screen, GREEN, ball_center, ball_radius)
# -----Ball-----

# 在知道發生碰撞的基礎上，加上反射的功能
# 反射的條件:
#   若碰到邊，則以邊的垂直向量為法線反射
#   若碰到角，則以 (1, 1) or (1, -1) 的方向為法線反射
# FIXME
# 註: 這邊要做好測試，測試方式待想
# -----Collision-----
def reflect(a, b):
    p = np.array(b) * (np.dot(a, b) / np.dot(b, b))
    return a - 2*p

def collision():
    global block_width, ball_center, block_center, ball_radius, ball_v
    block_hw = block_width / 2
    block_hh = block_width / 2

    u = ball_center - block_center
    u_abs = np.abs(u)
    u_sign = np.sign(u)
    
    if (u_abs <= (block_hw, block_hh)).any():
        (dir_x, dir_y) = (u_abs <= (block_hw + ball_radius, block_hh + ball_radius)) & np.flip(u_abs <= (block_hw, block_hh))
        if dir_x:
            ball_center = np.around(ball_center - ball_v)
            ball_v = reflect(ball_v, (1,0))
            return
        elif dir_y:
            ball_center = np.around(ball_center - ball_v)
            ball_v = reflect(ball_v, (0,1))
            return

    dist = np.linalg.norm(u_abs - (block_hw, block_hh))

    if dist <= ball_radius:
        ball_center = np.around(ball_center - ball_v)
        if np.dot(ball_v * u_sign, (1, 1)) < 0:
            ball_v = reflect(ball_v, u_sign)
        elif np.dot(ball_v * u_sign, (1, 0)) < 0:
            ball_v = reflect(ball_v, (1, 0))
        else:
            ball_v = reflect(ball_v, (0, 1))
        return
# -----Collision-----

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    
    pygame.draw.rect(screen, block_color, rect)

    collision()
    move_ball()

    pygame.display.update()
    clock.tick(60)
