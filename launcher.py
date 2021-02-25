import pygame, math, random
from ball import Ball

pos_y = 520
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
    
    def launch_balls(self, ball_group, pic_path):
        v0 = self.v0
        angle = self.angle
        vx = v0 * math.cos(angle)
        vy = v0 * math.sin(angle) * -1
        
        ball = Ball(self.pos, (vx, vy), pic_path)
        ball_group.add(ball)
    
    def set_pos_x(self, x):
        self.pos = (round(x), self.pos[1])


