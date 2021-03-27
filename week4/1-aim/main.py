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

# 這裡先重新定義視窗大小，比較好看一點
#   SCREEN_WIDTH = 420
#   SCREEN_HEIGHT = 540
# 註: 我有偷偷改了邊界的 Block
blocks = pygame.sprite.Group()
blocks.add(Block((SCREEN_WIDTH//2, -2*BALL_R), (SCREEN_WIDTH, 2*BALL_R)))   # top
blocks.add(Block((-2*BALL_R, SCREEN_HEIGHT//2), (2*BALL_R, SCREEN_HEIGHT))) # left
blocks.add(Block((SCREEN_WIDTH + 2*BALL_R, SCREEN_HEIGHT//2), (2*BALL_R, SCREEN_HEIGHT)))   # right

balls = pygame.sprite.Group()

launcher = Launcher()

# 這裡的目的是要讓他們想一下整個遊戲流程，想完之後再來繼續改寫程式
# 預設遊戲流程 
#   aim -> launch_hit -> new_block -> game_over
#    ^----------------------|
# 當然可以有他們自己的流程，這裡只是舉例
# 
# 有了遊戲流程之後，讓他們想一下要怎麼實現遊戲流程?
#  -> 這裡是用 state 來讓 while loop 來跑指定的流程
# 
# 也可以想想每個流程換到下一個流程的觸發條件是甚麼?

state = "aim"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 這裡做到按空白就結束即可
    # 順便告訴他們，寫 code 不要貪心，寫好一步測試一步，可以省去很多抵 bug 的時間
    if state == "aim":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            launcher.tilt_left()
            
        elif keys[pygame.K_RIGHT]:
            launcher.tilt_right()
        
        elif keys[pygame.K_SPACE]:
            state = "game_over"         
        
    elif state == "game_over":
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)
    blocks.draw(screen)
    balls.draw(screen)
    launcher.draw(screen)

    pygame.display.update()
    clock.tick(60)
