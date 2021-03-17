import sys
import pygame
import random
from utils import *
from block import *
from ball import *
from launcher import *
from functions import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("test test")

blocks = pygame.sprite.Group()
blocks.add(Wall((SCREEN_WIDTH//2, -2*BALL_R), (SCREEN_WIDTH, 2*BALL_R)))    # top
blocks.add(Wall((-2*BALL_R, SCREEN_HEIGHT//2), (2*BALL_R, SCREEN_HEIGHT)))  # left
blocks.add(Wall((SCREEN_WIDTH + 2*BALL_R, SCREEN_HEIGHT//2), (2*BALL_R, SCREEN_HEIGHT)))    # right

balls = pygame.sprite.Group()

launcher = Launcher()

# 預設遊戲流程 
#   aim -> launch_hit -> new_block -> game_over
#    ^----------------------|

# new_block 需要做的事:
#   1. 隨機產生方塊
#   2. 移動方塊
#      註: 三面牆壁不需要移動，所以我用 class Wall(Block)，並 overload move_block()
#   3. 如果 block 碰到最下面，結束遊戲

level = 1
# 一開始的 state 改成 new_block
state = "new_block"
frame_counter = 0
launched_balls = 0
x_setted = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if state == "aim":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            launcher.tilt_left()
            
        elif keys[pygame.K_RIGHT]:
            launcher.tilt_right()
        
        elif keys[pygame.K_SPACE]:
            state = "launch_hit"

    elif state == "launch_hit":
        if launched_balls < level:
            if frame_counter % 4 == 0:
                launcher.launch_one_ball(balls)
                launched_balls += 1

            frame_counter += 1
    
        for ball in balls:
            for block in blocks:
                collision(ball, block)
        balls.update()
        blocks.update()

        if not x_setted and launched_balls >= level and Ball.first_killed_x:
            launcher.set_pos_x(Ball.first_killed_x)
            x_setted = True

        keys = pygame.key.get_pressed()
        if len(balls) == 0 or keys[pygame.K_UP]:
            balls.empty()
            Ball.first_killed_x = None
            frame_counter = 0
            launched_balls = 0
            x_setted = False
            level += 1
            state = "new_block"

    elif state == "new_block":
        for i in range(7):
            # 若場面上的方塊大於8個，每一個位子有0.3的機率生成方塊，否則是0.6
            if len(blocks) > 8:
                prob = 0.3
            else:
                prob = 0.6

            if random.random() < prob:
                block = Block((BLOCK_WIDTH*(i+0.5),BLOCK_WIDTH*0.5),  BLOCK_SIZE)
                blocks.add(block)

        state = 'aim'

        for block in blocks:
            if block.move_down():
                state = 'game_over'
                
        
    elif state == "game_over":
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)
    blocks.draw(screen)
    balls.draw(screen)
    launcher.draw(screen)

    pygame.display.update()
    clock.tick(60)
