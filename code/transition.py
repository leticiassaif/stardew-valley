import pygame
from settings import *

class Transition:
    def __init__(self, reset, player):
        
        #setup
        self.display_surface = pygame.display.get_surface()
        self.reset = reset
        self.player = player

        #overlay image
        self.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.color = 255 #0 preto 255 branco
        self.speed = -1

    def play(self):
        
        self.color += self.speed #vai de branco a preto
        if self.color <= 00:
            self.speed *= -1 #vai de preto a branco
            self.color = 0
            self.reset()
        if self.color > 255:
            self.color = 255
            self.player.sleep = False
            self.speed = -2

        self.image.fill((self.color, self.color, self.color)) #r,g,b
        self.display_surface.blit(self.image,(0, 0), special_flags = pygame.BLEND_RGB_MULT) #deixa 255 invisível