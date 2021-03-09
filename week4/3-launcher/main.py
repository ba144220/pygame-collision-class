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

# -----Block-----
blocks = pygame.sprite.Group()
blocks.add(Block((300, 300), (100, 100), BLUE))

blocks.add(Block((1, 300), (2, SCREEN_HEIGHT), BLUE))
blocks.add(Block((SCREEN_WIDTH-1, 300), (2, SCREEN_HEIGHT), BLUE))
blocks.add(Block((300, 1), (SCREEN_WIDTH, 2), BLUE))
blocks.add(Block((300, SCREEN_HEIGHT-1), (SCREEN_WIDTH, 2), BLUE))
# -----Block-----

# -----Ball-----
balls = pygame.sprite.Group()
# -----Ball-----

# -----Launcher-----
launcher = Launcher()
# -----Launcher-----
level = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    if len(balls) < level:
        launcher.launch_one_ball(balls)
    
    for ball in balls:
        for block in blocks:
            collision(ball, block)
    balls.update()

    blocks.draw(screen)
    balls.draw(screen)
    launcher.draw(screen)

    pygame.display.update()
    clock.tick(60)
