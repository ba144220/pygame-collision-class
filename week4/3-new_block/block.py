import pygame
from utils import *
import numpy as np

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface(size)
        # 這裡稍微改變一下方塊著色，讓它周圍有個縫隙，比較好看
        # 但判斷 collision 範圍 self.rect 沒變
        pygame.draw.rect(self.image, BLOCK_COLOR, ((1, 1), (size[0] - 2, size[1] - 2)))
        self.rect = self.image.get_rect()
        self.rect.center = np.around(pos)

    def move_down(self):
        self.rect.centery += BLOCK_WIDTH
        return self.rect.centery >= SCREEN_HEIGHT - BLOCK_WIDTH

class Wall(Block):
    def __init__(self, pos, size):
        super().__init__(pos, size)

    def move_down(self):
        return



