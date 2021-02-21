import pygame, math

block_width = 48

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super().__init__()
    
        self.image = pygame.Surface([block_width,block_width])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (round(pos[0]), round(pos[1]))
        self.x0 = self.rect.center[0] - self.rect.width*0.5
        self.x1 = self.rect.center[0] + self.rect.width*0.5
        self.y0 = self.rect.center[1] - self.rect.width*0.5
        self.y1 = self.rect.center[1] + self.rect.width*0.5

        

    
