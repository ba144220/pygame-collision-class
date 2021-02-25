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
screen_width = 420
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


# Balls
ball_group = pygame.sprite.Group()
'''
for i in range(20):
    #ball = Ball((60+32*i,300-8*i), (4,-1), "ball_1.png")
    ball = Ball((random.randrange(100, screen_width-100), random.randrange(300,screen_height-100)), (8.0,-1.0), "./ball_1.png")
    ball_group.add(ball)
'''

# Blocks
block_group = pygame.sprite.Group()
block1 = Block((180,90),  58,  1)
block2 = Block((240,150),  58,  2)
block3 = Block((240, 210),  58, 3)
block_top = Block((210, -210),  422, -1 )
block_left = Block((-270,270),   542,  -2)
block_right = Block((690, 270),   542,  -3)
block_group.add(block1)
block_group.add(block_left)
block_group.add(block_right)
block_group.add(block_top)
block_group.add(block2)
block_group.add(block3)



state = 'aim'  # launch hit new_block move_block 
launch_counter = 0
ball_counter = 0
first_killed_ball_x = screen_width //2
level = 10

# Launcher
launcher = Launcher(first_killed_ball_x, 8)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if state == 'aim':
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            launcher.tilt_left()
            
        elif keys[pygame.K_RIGHT]:
            launcher.tilt_right()
        
        elif keys[pygame.K_SPACE]:
            launcher.launch_balls(ball_group,"./ball_1.png")
            state = 'launch'
            launch_counter = 0
            ball_counter = 1

    elif state == 'launch':
        launch_counter += 1
        if launch_counter % 4 == 0:
            if ball_counter <= level:
                launcher.launch_balls(ball_group,"./ball_1.png")
                ball_counter += 1
            else:
                state = "hit"
                first_killed_ball_x = None
    elif state == "hit":
        if first_killed_ball_x == None:
            for ball in ball_group:
                first_killed_ball_x = ball.get_killed_x()
                if first_killed_ball_x != None:
                    launcher.set_pos_x(first_killed_ball_x)
                    break

        if len(ball_group) == 0:
            state = 'aim'

        


    
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
    

