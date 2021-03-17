import pygame
from utils import *
import numpy as np

class Block(pygame.sprite.Sprite):
    font = pygame.font.SysFont("Arial", 25)
    font.set_bold(True)

    def __init__(self, pos, size, number, double=False):
        super().__init__()
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.center = np.around(pos)
        self.number = number
        self.color = BLOCK_INIT_COLOR_DOUBLE if double else BLOCK_INIT_COLOR
        self.color_dif = (np.array(self.color) - BLOCK_FINAL_COLOR)/number
        self.blit_to_image()

    def blit_to_image(self):
        size = np.array(BLOCK_SIZE)
        pygame.draw.rect(self.image, self.color, ((1, 1), size - (2, 2)))
        pygame.draw.rect(self.image, BLACK, ((4, 4), size - (8, 8)))
        textSurf = self.font.render(str(self.number), True, self.color, BLACK)
        self.image.blit(textSurf, np.array(size)/2 - textSurf.get_rect().center)

    def move_down(self, v):
        self.rect.centery += v
        return self.rect.centery >= SCREEN_HEIGHT - BLOCK_WIDTH

    def collided(self):
        self.number -= 1
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



