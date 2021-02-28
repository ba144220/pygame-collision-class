import pygame, math

init_color = (229,51,103)
init_color_double = (0,200,255)
final_color = (247,242,100)

screen_width = 420
screen_height = 540

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size, number,  id, double=False):
        super().__init__()
        self.pos = pos
        self.image = pygame.Surface(size)
        
        self.rect = self.image.get_rect()
        self.rect.center = (round(pos[0]), round(pos[1]))
        self.number = number
        self.init_number = number
        

        if double:
            self.init_color = init_color_double
            self.color = init_color_double
        else:
            self.init_color = init_color
            self.color = init_color

        self.image.fill(self.color)


        self.x1 = round(self.rect.center[0] - self.rect.width*0.5)
        self.x2 = round(self.rect.center[0] + self.rect.width*0.5)
        self.y1 = round(self.rect.center[1] - self.rect.width*0.5)
        self.y2 = round(self.rect.center[1] + self.rect.width*0.5)
        self.id = id

        self.font = pygame.font.SysFont("Arial", 25)
        self.font.set_bold(True)
        self.textSurf = self.font.render(str(number), 1, (0,0,0))
        
        self.size = size
        tW = self.textSurf.get_width()
        tH = self.textSurf.get_height()
        self.image.blit(self.textSurf, [size[0]/2 - tW/2, size[1]/2 - tH/2])
    
    def hit(self):
        self.number -= 1
        if self.number == 0:
            self.kill()
    
    def update_color(self):
        i_c = self.init_color
        f_c = final_color
        i_n = self.init_number
        c_n = self.number
        color = [0,0,0]
        for i in range(3):
            color[i] = round((i_c[i]*(c_n) + f_c[i]*(i_n-c_n))/i_n)
        self.color = (color[0], color[1], color[2])
        
    
    def update(self):
        # position related updates
        self.rect.center = (round(self.pos[0]), round(self.pos[1]))
        self.x1 = round(self.rect.center[0] - self.rect.width*0.5)
        self.x2 = round(self.rect.center[0] + self.rect.width*0.5)
        self.y1 = round(self.rect.center[1] - self.rect.width*0.5)
        self.y2 = round(self.rect.center[1] + self.rect.width*0.5)

        # display related updates
        if self.number > 0:
            self.update_color()

        self.image.fill(self.color)
        pygame.draw.rect(self.image, (0,0,0), (4,4,self.size[0]-8, self.size[1]-8))
        self.textSurf = self.font.render(str(self.number), 1, self.color)
        tW = self.textSurf.get_width()
        tH = self.textSurf.get_height()
        self.image.blit(self.textSurf, [self.size[0]/2 - tW/2, self.size[1]/2 - tH/2])
    
    def move_down(self, v):
        # 牆壁的self.number都小於0，他們不能移動
        if self.number >= 0:
            self.pos = (self.pos[0], self.pos[1] + v)
    
    def get_pos_y(self):
        return self.pos[1]
            




        

    
