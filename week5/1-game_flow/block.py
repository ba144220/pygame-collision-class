import pygame
from utils import *
import numpy as np

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(BLUE)
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



