import pygame, sys

from block_ball_detect import *
from ball import Ball
from block import Block
pygame.init()

# Color
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,200)
LIGHT_BLUE = (0,200,255)
RED = (200,0,0)
GREEN = (0,200,0)

# Screen
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


# Balls
ball_group = pygame.sprite.Group()
for i in range(10):
    ball = Ball((80+32*i,500-6*i), (8,-1.5), "ball_1.png")
    ball_group.add(ball)

# Blocks
block_group = pygame.sprite.Group()
block1 = Block((200,100), BLUE, 1)
block2 = Block((200,150), GREEN, 2)
block3 = Block((250, 200), BLUE, 3)
block_group.add(block1)
block_group.add(block2)
block_group.add(block3)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for bl in ball_group:
        bl.margin_collide_detect()
        for bk in block_group:
            ball_block_detect(bl, bk)

    ball_group.update()
    screen.fill(BLACK)

    block_group.draw(screen)
    ball_group.draw(screen)

    pygame.display.flip()
    
    clock.tick(60)

