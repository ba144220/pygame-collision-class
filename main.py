import pygame, sys, random

from block_ball_detect import *
from ball import Ball
from block import Block
from launcher import Launcher
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
for i in range(20):
    #ball = Ball((60+32*i,300-8*i), (4,-1), "ball_1.png")
    ball = Ball((random.randrange(100, screen_width-100), random.randrange(300,screen_height-100)), (8.0,-1.0), "./ball_1.png")
    ball_group.add(ball)

# Blocks
block_group = pygame.sprite.Group()
block1 = Block((200,100),  48,  1)
block2 = Block((200,150),  48,  2)
block3 = Block((250, 200),  48, 3)
block_top = Block((200, -200),  400, -1 )
block_left = Block((-400,400),   800,  -2)
block_right = Block((800, 400),   800,  -3)
block_group.add(block1)
block_group.add(block_left)
block_group.add(block_right)
block_group.add(block_top)
block_group.add(block2)
#block_group.add(block3)

# Launcher
launcher = Launcher(screen_width//2, 10)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        launcher.tilt_left()
        
    elif keys[pygame.K_RIGHT]:
        launcher.tilt_right()
    
    for bl in ball_group:
        for bk in block_group:
            ball_block_detect(bl, bk)

    ball_group.update()

    screen.fill(BLACK)

    launcher.draw(screen)

    block_group.draw(screen)
    ball_group.draw(screen)

    pygame.display.flip()
    
    clock.tick(60)
    

