import pygame
from utils import *
import numpy as np

class Block(pygame.sprite.Sprite):
    # 傳入參數增加了 number
    def __init__(self, pos, size, number):
        super().__init__()
        self.image = pygame.Surface(size)
        pygame.draw.rect(self.image, BLOCK_COLOR, ((1, 1), (size[0] - 2, size[1] - 2)))
        self.rect = self.image.get_rect()
        self.rect.center = np.around(pos)
        # 增加 self.number
        self.number = number

    def move_down(self):
        self.rect.centery += BLOCK_WIDTH
        return self.rect.centery >= SCREEN_HEIGHT - BLOCK_WIDTH

    # 增加發生碰撞時會呼叫的函式
    def collided(self):
        self.number -= 1
        if self.number == 0:
            self.kill()

class Wall(Block):
    def __init__(self, pos, size):
        # 預設 Wall.number = -1
        super().__init__(pos, size, -1)

    def move_down(self):
        return

    # Wall 發生碰撞時不用做事
    def collided(self):
        return

