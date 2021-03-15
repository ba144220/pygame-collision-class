import sys
import pygame
pygame.init()
import random
from utils import *
from block import *
from ball import *
from launcher import *
from functions import *


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("test test")

blocks = pygame.sprite.Group()
block_top = Wall((210, -210), (422,422))
block_left = Wall((-270,270), (542,542))
block_right = Wall((690, 270), (542,542))
blocks.add(block_top)
blocks.add(block_left)
blocks.add(block_right)

balls = pygame.sprite.Group()
launcher = Launcher()

level = 1
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
            level += 50
            state = 'new_block'

    elif state == "new_block":
        for i in range(7):
            # 若場面上的方塊大於8個，每一個位子有0.3的機率生成方塊，否則是0.6
            if len(blocks) > 8:
                prob = 0.3
            else:
                prob = 0.6

            if random.random() < prob:
                if random.random() < 0.2:
                    block = Block((BLOCK_WIDTH*(i+0.5),BLOCK_WIDTH*0.5),  BLOCK_SIZE, 2*level, True)
                else:  
                    block = Block((BLOCK_WIDTH*(i+0.5),BLOCK_WIDTH*0.5),  BLOCK_SIZE, level)
                blocks.add(block)

        state = 'move_block'

    elif state == "move_block":
        for block in blocks:
            if block.move_down(2):
                state = 'game_over'

        frame_counter += 1
        if frame_counter >= BLOCK_WIDTH // 2:
            frame_counter = 0
            state = "aim"
                
        
    elif state == "game_over":
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)
    blocks.draw(screen)
    balls.draw(screen)
    launcher.draw(screen)

    pygame.display.update()
    clock.tick(60)
