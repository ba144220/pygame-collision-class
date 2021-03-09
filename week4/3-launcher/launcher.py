import pygame
import numpy as np
from math import pi, cos, sin
from utils import *
from ball import Ball

class Launcher():
    def __init__(self):
        self.pos = np.array((SCREEN_WIDTH/2, LAUNCHER_Y))
        self.angle = pi/4
        self.angle_dif = pi/90
        self.angle_min = pi/12
    
    def tilt_right(self):
        if self.angle >= self.angle_min:
            self.angle -= self.angle_dif

    def tilt_left(self):
        if self.angle <= pi - self.angle_min:
            self.angle += self.angle_dif

    def draw(self, screen):
        end_pos = self.pos + LAUNCHER_R_BARREL * np.array((cos(self.angle), -1*sin(self.angle)))
        pygame.draw.line(screen, LAUNCHER_COLOR, self.pos, end_pos)
        pygame.draw.circle(screen, WHITE, self.pos, LAUNCHER_R_IN, 1)
    
    def launch_one_ball(self, ball_group):
        angle = self.angle
        vx = BALL_V * cos(angle)
        vy = BALL_V * sin(angle) * -1
        
        ball = Ball(self.pos, (vx, vy))
        ball_group.add(ball)

    def set_pos_x(self, x):
        x = 50 if x < 50 else SCREEN_WIDTH - 50 if x > SCREEN_WIDTH - 50 else x
        self.pos[0] = round(x)

