import pygame, math
from vector_operations import *

screen_width = 400
screen_height = 600


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, v, pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()
        self.rect.center = (round(pos[0]), round(pos[1]))
        self.pos = pos
        self.v = v # tuple
        
        self.r = self.rect.width * 0.5
        self.collided = []

    def update(self):
        self.pos = (self.pos[0]+self.v[0], self.pos[1]+self.v[1])
        self.rect.center = (round(self.pos[0]), round(self.pos[1]))
    
        if self.pos[1] >= screen_height:
            print('margin bottom')
            self.kill()
    



