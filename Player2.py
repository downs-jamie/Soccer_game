import pygame
from pygame.sprite import Sprite

class Player2(Sprite):
    def __init__(self, screen):
        super(Player2,self). __init__()
        self.image = pygame.image.load("soccer_player2.png")
        self.x = 1147
        self.y = 415
        self.width = 45
        self.height = 81
        self.speed = 4.9
        self.screen = screen
        self.has_ball = False

    def draw_me(self):
        self.screen.blit(self.image, [self.x, self.y])