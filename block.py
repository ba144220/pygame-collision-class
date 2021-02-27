import pygame, math

init_color = (0,200,255)

screen_width = 420
screen_height = 540

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size, number,  id):
        super().__init__()
    
        self.image = pygame.Surface(size)
        self.image.fill(init_color)
        self.rect = self.image.get_rect()
        self.rect.center = (round(pos[0]), round(pos[1]))
        self.number = number

        self.color = init_color
        self.x1 = round(self.rect.center[0] - self.rect.width*0.5)
        self.x2 = round(self.rect.center[0] + self.rect.width*0.5)
        self.y1 = round(self.rect.center[1] - self.rect.width*0.5)
        self.y2 = round(self.rect.center[1] + self.rect.width*0.5)
        self.id = id

        self.font = pygame.font.SysFont("Arial", 25)
        self.textSurf = self.font.render(str(number), 1, (0,0,0))
        
        self.size = size
        tW = self.textSurf.get_width()
        tH = self.textSurf.get_height()
        self.image.blit(self.textSurf, [size[0]/2 - tW/2, size[1]/2 - tH/2])
    
    def hit(self):
        self.number -= 1
        if self.number == 0:
            self.kill()
    
    def update(self):
        self.image.fill(init_color)
        self.textSurf = self.font.render(str(self.number), 1, (0,0,0))
        tW = self.textSurf.get_width()
        tH = self.textSurf.get_height()
        self.image.blit(self.textSurf, [self.size[0]/2 - tW/2, self.size[1]/2 - tH/2])



        

    
