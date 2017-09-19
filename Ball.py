

import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, screen):
        super(Ball,self). __init__()
        self.image = pygame.image.load("soccer_ball.png")
        self.x = 639
        self.y = 406
        self.speed = 1
        self.screen = screen

    def draw_me(self):
        self.screen.blit(self.image, [self.x, self.y])