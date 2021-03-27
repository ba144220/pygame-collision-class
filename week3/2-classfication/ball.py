import pygame
import numpy as np
from utils import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, v):
        super().__init__()
        self.image = pygame.Surface((2*BALL_R, 2*BALL_R), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BALL_COLOR, (BALL_R, BALL_R), BALL_R)
        self.rect = self.image.get_rect()
        self.rect.center = np.around(pos)
        self.v = np.array(v)
        
    def update(self):
        self.rect.center = np.around(self.rect.center + self.v)
