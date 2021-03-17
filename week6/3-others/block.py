import pygame
from utils import *
import numpy as np

class Block(pygame.sprite.Sprite):
    font = pygame.font.SysFont("Arial", 25)
    font.set_bold(True)

    # 增加 self.color 來記錄現在的顏色
    # 增加 self.color 來記錄每次要改變多少顏色
    # utils.py 增加
    #   BLOCK_INIT_COLOR = (229, 51, 103)
    #   BLOCK_INIT_COLOR_DOUBLE = (0, 200, 255)
    #   BLOCK_FINAL_COLOR = (247, 242, 100)
    # 刪除
    #   BLOCK_COLOR = BLUE
    def __init__(self, pos, size, number, double=False):
        super().__init__()
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.center = np.around(pos)
        self.number = number
        self.color = np.array(BLOCK_INIT_COLOR_DOUBLE if double else BLOCK_INIT_COLOR)
        self.color_dif = (self.color - BLOCK_FINAL_COLOR)/number
        self.blit_to_image()

    # 這裡的 BLOCK_COLOR 都變成 self.color
    def blit_to_image(self):
        size = np.array(BLOCK_SIZE)
        pygame.draw.rect(self.image, self.color, ((1, 1), size - (2, 2)))
        pygame.draw.rect(self.image, BLACK, ((4, 4), size - (8, 8)))
        textSurf = self.font.render(str(self.number), True, self.color, BLACK)
        self.image.blit(textSurf, size/2 - textSurf.get_rect().center)

    def move_down(self, v):
        self.rect.centery += v
        return self.rect.centery >= SCREEN_HEIGHT - BLOCK_WIDTH

    def collided(self):
        self.number -= 1
        # 每次碰撞都改變顏色
        self.color = self.color - self.color_dif
        if self.number == 0:
            self.kill()
        else:
            self.blit_to_image()


class Wall(Block):
    def __init__(self, pos, size):
        super().__init__(pos, size, -1)

    def move_down(self, v):
        return
    
    def collided(self):
        return



