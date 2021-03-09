import sys
import pygame
import numpy as np

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,200)
GREEN = (0,200,0)
RED = (200,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("test test")

# -----Block-----
class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = pos

blocks = pygame.sprite.Group()
blocks.add(Block((300, 300), (100, 100), BLUE))

blocks.add(Block((1, 300), (2, SCREEN_HEIGHT), BLUE))
blocks.add(Block((SCREEN_WIDTH-1, 300), (2, SCREEN_HEIGHT), BLUE))
blocks.add(Block((300, 1), (SCREEN_WIDTH, 2), BLUE))
blocks.add(Block((300, SCREEN_HEIGHT-1), (SCREEN_WIDTH, 2), BLUE))

# -----Block-----

# -----Ball-----
class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, radius, color, v):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2*radius, 2*radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.v = np.array(v)
        
    def update(self):
        pygame.sprite.Sprite.update(self)
        self.rect.center = np.remainder(self.rect.center + self.v, [SCREEN_WIDTH, SCREEN_HEIGHT])

balls = pygame.sprite.Group()
balls.add(Ball((40.0,200.0), 20, GREEN, (6.0,3.0)))

# -----Ball-----

# -----Collision-----
def reflect(a, b):
    p = np.array(b) * (np.dot(a, b) / np.dot(b, b))
    return a - 2*p

def collision(ball, block):
    block_hw = block.rect.width / 2
    block_hh = block.rect.height / 2
    ball_radius = ball.rect.width / 2

    v = np.array(ball.rect.center) - np.array(block.rect.center)
    v_abs = np.abs(v)

    if (v_abs <= (block_hw, block_hh)).any():
        (dir_x, dir_y) = (v_abs <= (block_hw + ball_radius, block_hh + ball_radius)) & np.flip(v_abs <= (block_hw, block_hh))
        if dir_x:
            print("reflect x")
            ball.v = reflect(ball.v, (1,0))
            return
        elif dir_y:
            print("reflect y")
            ball.v = reflect(ball.v, (0,1))
            return
            
    dist = np.linalg.norm(v_abs - (block_hw, block_hh))

    if dist <= ball_radius:
        if np.prod(v) > 0:
            print("reflect (1, 1)")
            ball.v = reflect(ball.v, (1,1))
        else:
            print("reflect (1, -1)")
            ball.v = reflect(ball.v, (1,-1))
# -----Collision-----

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
