import pygame, math

init_color = (0,200,255)

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, width,  id):
        super().__init__()
    
        self.image = pygame.Surface([width,width])
        self.image.fill(init_color)
        self.rect = self.image.get_rect()
        self.rect.center = (round(pos[0]), round(pos[1]))

        self.color = init_color
        self.x1 = round(self.rect.center[0] - self.rect.width*0.5)
        self.x2 = round(self.rect.center[0] + self.rect.width*0.5)
        self.y1 = round(self.rect.center[1] - self.rect.width*0.5)
        self.y2 = round(self.rect.center[1] + self.rect.width*0.5)
        self.id = id


        

    
