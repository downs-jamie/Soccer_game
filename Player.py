import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, screen):
        super(Player,self). __init__()
        self.image = pygame.image.load("soccer_player.png")
        self.x = 100
        self.y = 415
        self.width = 45
        self.height = 81
        self.speed = 8
        self.screen = screen

    def draw_me(self):
        self.screen.blit(self.image, [self.x, self.y])