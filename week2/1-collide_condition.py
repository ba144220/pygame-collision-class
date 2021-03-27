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

# 為了要讓判斷 collision、模組化方便，把屬於 block 的性質獨立出來
# -----Block-----
block_width = 100
block_center = (300, 300)
# 這裡 (250, 250) 比較尷尬，可以不改沒關係，包成 class 之後 block 位置不會這樣設
rect = pygame.Rect((250, 250), (block_width, block_width))
pygame.draw.rect(screen, BLUE, rect)
# -----Block-----

# 為了判斷 collision，繼續把 ball_radius 獨立出來
# 好一點的話，也要把 ball_color 獨立出來，因為那是屬於 ball 的一種性質，不應該出現在 function 裡面
# 註: 把 ball_color 等屬於 ball 的性質，會在講到 class 的時候更加清楚，這裡只是先提
# 可以讓他們把 ball 限制在畫面裡面
# -----Ball-----
ball_center = np.array((40.0,200.0))
ball_radius = 20
ball_color = GREEN
ball_v = np.array((6.0,3.0))

def move_ball():
    global ball_center, ball_color, ball_radius
    ball_center = ball_center + ball_v
    ball_center = np.remainder(ball_center, [SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.draw.circle(screen, ball_color, ball_center, ball_radius)
# -----Ball-----

# 這裡要讓他們想: 
#   要在哪個地方判斷 collision? (在 While)
#   判斷 collision 需要哪些參數?
# 這裡只要判斷有碰撞，並在碰撞時，印出 collide 即可，不須寫反射判斷
# -----Collision-----
def collision():
    global block_width, ball_center, block_center, ball_radius, ball_v
    block_hw = block_width / 2

    v = ball_center - block_center
    v_abs = np.abs(v)

    if (v_abs <= block_hw).any():
        if ((v_abs <= block_hw + ball_radius) & np.flip(v_abs <= block_hw)).any():
            print("collide")
            return
            
    dist = np.linalg.norm(v_abs - (block_hw, block_hw))

    if dist <= ball_radius:
        print("collide")
# -----Collision-----

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    
    pygame.draw.rect(screen, BLUE, rect)

    collision()
    move_ball()

    pygame.display.update()
    clock.tick(60)
