import sys
import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,200)
GREEN = (0,200,0)
RED = (200,0,0)

# 這裡要講說，為了共用參數、讀去參數方便，會把一些參數另外寫好
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("test test")

rect = pygame.Rect((250, 250), (100, 100))
pygame.draw.rect(screen, BLUE, rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
