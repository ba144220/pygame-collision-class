import sys
import pygame
import numpy as np
# from vector_operations import reflect as rf

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
ball_radius = 20
ball_color = GREEN
ball_v = np.array((6.0,3.0))

def move_ball():
    global ball_center, ball_color, ball_radius
    ball_center = ball_center + ball_v
    ball_center = np.remainder(ball_center, [SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.draw.circle(screen, ball_color, ball_center, ball_radius)
# -----Ball-----

# -----Collision-----
def reflect(a, b):
    p = np.array(b) * (np.dot(a, b) / np.dot(b, b))
    return a - 2*p

def collision():
    global block_width, ball_center, block_center, ball_radius, ball_v
    block_hw = block_width / 2

    v = ball_center - block_center
    v_abs = np.abs(v)

    if (v_abs <= block_hw).any():
        (dir_x, dir_y) = (v_abs <= block_hw + ball_radius) & np.flip(v_abs <= block_hw)
        if dir_x:
            print("reflect x")
            ball_v = reflect(ball_v, (1,0))
            return
        elif dir_y:
            print("reflect y")
            ball_v = reflect(ball_v, (0,1))
            return
            
    dist = np.linalg.norm(v_abs - (block_hw, block_hw))

    if dist <= ball_radius:
        if np.prod(v) > 0:
            print("reflect (1, 1)")
            ball_v = reflect(ball_v, (1,1))
        else:
            print("reflect (1, -1)")
            ball_v = reflect(ball_v, (1,-1))
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
