import pygame
from settings import *

class Level:
    def __init__(self):
        # get the display surface
        self.display_surf = pygame.display.get_surface()
        # sprite groups
        self.all_sprites = pygame.sprite.Group() # draw & update all sprites in game

    def run(self, dt):
        self.display_surf.fill("black")
        self.all_sprites.draw(self.display_surf)
        self.all_sprites.update()