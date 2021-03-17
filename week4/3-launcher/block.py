import pygame
from utils import *
import numpy as np

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(BLOCK_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = np.around(pos)

