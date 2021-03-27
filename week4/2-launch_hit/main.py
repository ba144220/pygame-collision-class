import sys
import pygame
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
blocks.add(Block((SCREEN_WIDTH//2, -2*BALL_R), (SCREEN_WIDTH, 2*BALL_R)))   # top
blocks.add(Block((-2*BALL_R, SCREEN_HEIGHT//2), (2*BALL_R, SCREEN_HEIGHT))) # left
blocks.add(Block((SCREEN_WIDTH + 2*BALL_R, SCREEN_HEIGHT//2), (2*BALL_R, SCREEN_HEIGHT)))   # right

balls = pygame.sprite.Group()

launcher = Launcher()

# 預設遊戲流程 
#   aim -> launch_hit -> new_block -> game_over
#    ^----------------------|

# 以下是我的 launch_hit 想法 & 注意事項，僅供參考
#   1. 每 4 幀發射一顆球
#   2. 當球 y座標 > SCREEN_HEIGHT - BALL_R，該球就要被刪掉
#      可以使用 pygame.sprite.Sprite.kill() 來刪除 pygame.sprite.Sprite
#   3. 第一顆球落下的 x 座標為 launcher 座標 (Launcher.set_pos_x() 有自己限制座標在 50 ~ SCREEN_WIDTH - 50 之間)
"""    這裡要想一下     """
#      我的做法是當第一顆球被刪掉(kill)時，把 Ball.first_killed_x(class member) 設為該球座標
#      當所有球都發射完時，再來設定 launcher 座標，這樣才不會射到一半換位置
#      註: 不用 lan(balls) 來知道發射了多少球，是因為有可能還沒發射完，就有球被刪掉，形成無限循環
#   4. 當所有球都射完 or 按上鍵，換下一個 state

level = 1
state = "aim"
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
    
    if state == "launch_hit":
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
