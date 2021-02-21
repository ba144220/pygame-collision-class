import pygame, sys
pygame.init()

# Color
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,200)
LIGHT_BLUE = (0,200,255)
RED = (200,0,0)
GREEN = (0,200,0)

# Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(BLACK)

    pygame.display.flip()
    clock.tick(60)

