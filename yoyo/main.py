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

# Blocks
block_width = screen_width//7
block_size = (block_width-2, block_width-2)
block_group = pygame.sprite.Group()

block_top = Block((210, -210),  (422,422), -1, -1 )
block_left = Block((-270,270),   (542,542), -1, -2)
block_right = Block((690, 270),    (542,542), -1,  -3)

block_group.add(block_left)
block_group.add(block_right)
block_group.add(block_top)



state = 'new_block'  # launch hit new_block move_block aim game_over
frame_counter = 0
ball_counter = 0
first_killed_ball_x = screen_width //2
level = 1
block_id = 1

# Launcher
launcher = Launcher(first_killed_ball_x, 8)



while True:

    # 按叉叉會結束程式
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
            launcher.launch_balls(ball_group)

            # 準備下一個state
            state = 'launch'
            frame_counter = 0
            ball_counter = 1



    elif state == 'launch':
        frame_counter += 1
        # 每四幀畫面發射一顆球
        if frame_counter % 4 == 0:
            # level 幾就有幾顆球
            if ball_counter < level:
                launcher.launch_balls(ball_group)
                ball_counter += 1
            else:
                state = "hit"
                first_killed_ball_x = None
        
    elif state == "hit":
        
        # 第一顆球落下的位置會是下一次發射的位置
        if first_killed_ball_x == None:
            for ball in ball_group:
                first_killed_ball_x = ball.get_killed_x()
                if first_killed_ball_x != None:
                    launcher.set_pos_x(first_killed_ball_x)
                    break
        # 所有的球都掉下來了 或 按up
        keys = pygame.key.get_pressed()
        if len(ball_group) == 0 or keys[pygame.K_UP]:
            for ball in ball_group:
                ball.kill()
            state = 'new_block'
            level += 1
    
    elif state == "new_block":
        for i in range(7):
            # 若場面上的方塊大於8個，每一個位子有0.3的機率生成方塊，否則是0.6
            if len(block_group) > 8:
                prob = 0.3
            else:
                prob = 0.6
            

            if random.random() < prob:
                if random.random() < 0.2:
                    block = Block((block_width*(i+0.5),block_width*0.5),  block_size, 2*level,  block_id, True)
                else:  
                    block = Block((block_width*(i+0.5),block_width*0.5),  block_size, level,  block_id)
                block_group.add(block)
                block_id += 1
        state = 'move_block'
        frame_counter = 0
        
    
    elif state == 'move_block':
        if frame_counter > 28:
            state = 'aim'
        for block in block_group:
            block.move_down(2)
            if block.get_pos_y() >= screen_height - block_width:
                state = 'game_over'
        
        frame_counter += 1

    elif state == 'game_over':
        pygame.quit()
        sys.exit()




        


    
    for bl in ball_group:
        for bk in block_group:
            ball_block_detect(bl, bk)

    ball_group.update()
    block_group.update()

    screen.fill(BLACK)

    launcher.draw(screen)

    block_group.draw(screen)
    ball_group.draw(screen)

    pygame.display.flip()
    
    clock.tick(60)
    

