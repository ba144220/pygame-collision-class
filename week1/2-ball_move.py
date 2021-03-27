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

# -----Block-----
rect = pygame.Rect((250, 250), (100, 100))
pygame.draw.rect(screen, BLUE, rect)
# -----Block-----

# 讓他們想一下，如果要讓一顆球移動，要怎麼做?
# 如果需要每幀都更新一次狀態，那需要紀錄跟運用 ball 的哪些基本訊息?
# 哪些動作要在 while 迴圈裡面做的? -> 為了方便閱讀，包成 function
# -----Ball-----
ball_center = np.array((40.0,200.0))
ball_v = np.array((6.0,3.0))

def move_ball():
    global ball_center, ball_v
    ball_center = ball_center + ball_v
    ball_center = np.remainder(ball_center, [SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.draw.circle(screen, GREEN, ball_center, 20)
# -----Ball-----

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, BLUE, rect)
    move_ball()

    pygame.display.update()
    clock.tick(60)
