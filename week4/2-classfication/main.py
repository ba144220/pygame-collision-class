import sys
import pygame
from block import *
from ball import *
from utils import *
from functions import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("test test")

# 幾個分檔要領:
#   不同的 class，不同檔 -> ball.py, block.py
#   程式會用到的 function 放別的檔 -> functions.py
#   各種共用參數放一個檔 -> utils.py
# 註: 分檔後記得 import

# -----Block-----
blocks = pygame.sprite.Group()
blocks.add(Block((300, 300), (100, 100)))

blocks.add(Block((1, 300), (2, SCREEN_HEIGHT)))
blocks.add(Block((SCREEN_WIDTH-1, 300), (2, SCREEN_HEIGHT)))
blocks.add(Block((300, 1), (SCREEN_WIDTH, 2)))
blocks.add(Block((300, SCREEN_HEIGHT-1), (SCREEN_WIDTH, 2)))
# -----Block-----

# -----Ball-----
balls = pygame.sprite.Group()
balls.add(Ball((40.0,200.0), (6.0,3.0)))
balls.add(Ball((80.0,200.0), (-6.0,3.0)))
# -----Ball-----

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    
    for ball in balls:
        for block in blocks:
            collision(ball, block)
    balls.update()

    blocks.draw(screen)
    balls.draw(screen)

    pygame.display.update()
    clock.tick(60)
