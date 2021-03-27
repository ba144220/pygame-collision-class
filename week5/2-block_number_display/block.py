import pygame
from utils import *
import numpy as np

# 要顯示字步驟:
#   1. 必須要有 pygame.font
#   2. 然後拿 pygame.font.render() 來產生一個 surface
#   3. 再拿這個 surface 去 塞進(blit) 目標的 surface(aka. Block.image)
#   註: 字體是沒有辦法直接 render 在現有的 surface(aka. Block.image) 上的
#       必須再創一個 surface 再 blit 進去 (我覺得小冗XD)

class Block(pygame.sprite.Sprite):
    font = pygame.font.SysFont("Arial", 25)
    font.set_bold(True)

    def __init__(self, pos, size, number):
        super().__init__()
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.center = np.around(pos)
        self.number = number
        self.blit_to_image()

    # 因為要畫出字體的步驟比較複雜，我把它額外用 function 包起來
    # 下面的 collided() 也會用到 (雖然會影響效能就是了：）)
    def blit_to_image(self):
        size = np.array(BLOCK_SIZE)
        pygame.draw.rect(self.image, BLOCK_COLOR, ((1, 1), size - (2, 2)))
        pygame.draw.rect(self.image, BLACK, ((4, 4), size - (8, 8)))
        textSurf = self.font.render(str(self.number), True, BLOCK_COLOR, BLACK)
        self.image.blit(textSurf, size/2 - textSurf.get_rect().center)

    def move_down(self):
        self.rect.centery += BLOCK_WIDTH
        return self.rect.centery >= SCREEN_HEIGHT - BLOCK_WIDTH

    def collided(self):
        self.number -= 1
        if self.number == 0:
            self.kill()
        # 每次碰撞都要更改數字
        else:
            self.blit_to_image()

class Wall(Block):
    def __init__(self, pos, size):
        super().__init__(pos, size, -1)

    def move_down(self):
        return

    def collided(self):
        return

