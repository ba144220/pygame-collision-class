import pygame, sys
from vector_operations import *
from ball import Ball
from block import Block
pygame.init()

# Color
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,200)
LIGHT_BLUE = (0,200,255)
RED = (200,0,0)
GREEN = (0,200,0)

# Screen
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


# Balls
ball_group = pygame.sprite.Group()
for i in range(10):
    ball = Ball((80+16*i,400-3*i), (8.0,-1.5), "ball_1.png")
    ball_group.add(ball)

# Blocks
block_group = pygame.sprite.Group()
block1 = Block((200,100), BLUE)
block2 = Block((200,150), GREEN)
block3 = Block((250, 200), BLUE)
block_group.add(block1)
block_group.add(block2)
block_group.add(block3)


def ball_block_detect(ball, block):
    ball_x, ball_y = ball.pos
    block_x, block_y = block.rect.center

    if ball_x >= block.x0 and ball_x <= block.x1:
        if ball_y >= block.y0 - ball.r and ball_y <= block.y0:
            print('block top')
            ball.v = reflect(ball.v, (0,-1))
        elif ball_y <= block.y1 + ball.r and ball_y >= block.y1:
            print('block bottom')
            ball.v = reflect(ball.v, (0,1))
    
    elif ball_y >= block.y0 and ball_y <= block.y1:
        if ball_x >= block.x0 - ball.r and ball_x <= block.x0:
            print('block left')
            ball.v = reflect(ball.v, (-1,0))
        elif ball_x <= block.x1 + ball.r and ball_x >= block.x1:
            print('block right')
            ball.v = reflect(ball.v, (1,0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for bl in ball_group:
        bl.margin_collide_detect()
        for bk in block_group:
            ball_block_detect(bl, bk)

    ball_group.update()
    screen.fill(BLACK)

    block_group.draw(screen)
    ball_group.draw(screen)

    pygame.display.flip()
    
    clock.tick(60)

