import pygame
import numpy as np
from utils import *

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
