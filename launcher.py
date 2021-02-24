import pygame, math

pos_y = 580
angle_dif = math.pi/90
angle_min = math.pi / 12

class Launcher():
    def __init__(self, pos_x, v0):
        super().__init__()
        self.pos = (pos_x, pos_y)
        self.angle = math.pi / 2
        self.R = 100
        self.r = 15
        self.v0 = v0
        self.color = (255,255,255)

    def tilt_right(self):
        if self.angle >= angle_min:
            self.angle -= angle_dif
    
    def tilt_left(self):
        if self.angle <= math.pi - angle_min:
            self.angle += angle_dif
    
    def draw(self, screen):
        R = self.R
        end_pos = (self.pos[0] + round(R*math.cos(self.angle)), self.pos[1] - round(R*math.sin(self.angle)))
        pygame.draw.line(screen, self.color, self.pos, end_pos)
        pygame.draw.circle(screen, (255,255,255), self.pos, self.r, 1)


