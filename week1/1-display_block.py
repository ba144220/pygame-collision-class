import sys
import pygame
from vector_operations import *

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,200)
GREEN = (0,200,0)
RED = (200,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("test test")

block_center = (300,300)
block_width = 100
block_color = BLUE

rect = pygame.Rect(0,0,1,1)
rect.width = block_width
rect.height = block_width
rect.center = block_center
pygame.draw.rect(screen, block_color, rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
