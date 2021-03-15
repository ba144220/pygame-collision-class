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

# 這次的目的是要讓他們加上 >1 顆球 & 四面牆
# 這裡就帶到 class 的使用時機

# 把 Block 跟 Ball 用 class 獨立出來
# 這裡要介紹一下 pygame.sprite.Sprite 的一些性質:
#   1. 被 pygame.sprite.Group 統一處理的單位 (顯示、更新都會透過 pygame.sprite.Group)
#   2. pygame.sprite.Group.add() 來將 pygame.sprite.Sprite 加入群組
#   3. pygame.sprite.Group.update() 來更新整個群組的 sprite
#      更新時，會呼叫 pygame.sprite.Sprite.update()，因此可以 overload
#   4. pygame.sprite.Group.draw() 來把整個群組的 sprite 畫出來
#   5. 在 pygame.sprite.Group.draw() 被呼叫時，pygame.sprite.Sprite 一定要有兩個 member:
#       (1) image: 一個 pygame.Surface，之後用來畫在 screen(pygame 視窗) 上的
#       (2) rect: 一個 pygame.Rect，整個 sprite 的範圍，其位置就是要畫在 screen 上的位置
# -----Block-----
class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size, color):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = pos

blocks = pygame.sprite.Group()
blocks.add(Block((300, 300), (100, 100), BLUE))

# 把四周的牆壁加進來
blocks.add(Block((1, 300), (2, SCREEN_HEIGHT), BLUE))
blocks.add(Block((SCREEN_WIDTH-1, 300), (2, SCREEN_HEIGHT), BLUE))
blocks.add(Block((300, 1), (SCREEN_WIDTH, 2), BLUE))
blocks.add(Block((300, SCREEN_HEIGHT-1), (SCREEN_WIDTH, 2), BLUE))

# -----Block-----

# -----Ball-----
class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, radius, color, v):
        super().__init__()
        self.image = pygame.Surface((2*radius, 2*radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.v = np.array(v)
        
    def update(self):
        self.rect.center = self.rect.center + self.v

# 加入多點球，測試 collision 有沒有 bug
balls = pygame.sprite.Group()
balls.add(Ball((40.0,200.0), 20, GREEN, (6.0,3.0)))
balls.add(Ball((80.0,200.0), 20, GREEN, (-6.0,3.0)))
# -----Ball-----

# -----Collision-----
def reflect(a, b):
    print(f"reflect {b}")
    p = np.array(b) * (np.dot(a, b) / np.dot(b, b))
    return a - 2*p

# 這裡記得將 collision 的傳入參數設成 ball, block
# 裡面的各種參數也改一改
def collision(ball, block):
    block_hw = block.rect.width / 2
    block_hh = block.rect.height / 2
    ball_radius = ball.rect.width / 2

    ball_v = ball.v
    ball_rect_center = np.array(ball.rect.center)

    u = ball_rect_center - block.rect.center
    u_abs = np.abs(u)
    u_sign = np.sign(u)
    
    if (u_abs <= (block_hw, block_hh)).any():
        (dir_x, dir_y) = (u_abs <= (block_hw + ball_radius, block_hh + ball_radius)) & np.flip(u_abs <= (block_hw, block_hh))
        if dir_x:
            ball.rect.center = np.around(ball_rect_center - ball_v)
            ball.v = reflect(ball_v, (1,0))
            return
        elif dir_y:
            ball.rect.center = np.around(ball_rect_center - ball_v)
            ball.v = reflect(ball_v, (0,1))
            return

    dist = np.linalg.norm(u_abs - (block_hw, block_hh))

    if dist <= ball_radius:
        ball.rect.center = np.around(ball_rect_center - ball_v)
        if np.dot(ball_v * u_sign, (1, 1)) < 0:
            ball.v = reflect(ball_v, u_sign)
        elif np.dot(ball_v * u_sign, (1, 0)) < 0:
            ball.v = reflect(ball_v, (1, 0))
        else:
            ball.v = reflect(ball_v, (0, 1))
        return
# -----Collision-----

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    
    # 既然有多個 ball, block，每幀都要判斷碰撞條件
    for ball in balls:
        for block in blocks:
            collision(ball, block)
    balls.update()

    blocks.draw(screen)
    balls.draw(screen)

    pygame.display.update()
    clock.tick(60)
