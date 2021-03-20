import sys
import pygame
from utils import *
from block import *
from ball import *
from launcher import *
from functions import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("test test")

# -----Block-----
blocks = pygame.sprite.Group()
blocks.add(Block((300, 300), (100, 100)))

blocks.add(Block((1, 300), (2, SCREEN_HEIGHT)))
blocks.add(Block((SCREEN_WIDTH-1, 300), (2, SCREEN_HEIGHT)))
blocks.add(Block((300, 1), (SCREEN_WIDTH, 2)))
blocks.add(Block((300, SCREEN_HEIGHT-1), (SCREEN_WIDTH, 2)))
# -----Block-----

# -----Ball-----
balls = pygame.sprite.Group()
# -----Ball-----

# 這裡 Launcher 有時間的話再給他們寫
# 沒時間的話，直接給他們 launcher.py，讓他們讀懂 code 後自己操作
# Launcher 要求:
#   class Ball 初始化條件 __init__(pos, v)，詳見 ball.py
# 
# 註: 增加了 utils.py 的一些定義
#   BALL_V = 8
#   LAUNCHER_Y = 520
#   LAUNCHER_R_IN = 15
#   LAUNCHER_R_BARREL = 100
#   LAUNCHER_COLOR = WHITE
# 
# 註: 可以改 __init__() 下 self.angle 來調整 Launcher 初始角度
# -----Launcher-----
launcher = Launcher()
# -----Launcher-----

level = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    if len(balls) < level:
        launcher.launch_one_ball(balls)
    
    for ball in balls:
        for block in blocks:
            collision(ball, block)
    balls.update()

    blocks.draw(screen)
    balls.draw(screen)
    launcher.draw(screen)

    pygame.display.update()
    clock.tick(60)
