import sys
import pygame
import numpy as np
from vector_operations import *

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, block_color, rect)
    move_ball()

    pygame.display.update()
    clock.tick(60)
