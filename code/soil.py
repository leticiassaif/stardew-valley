import pygame
from settings import *

class SoilLayer:
    def __init__(self, all_sprites):
        # sprites group
        self.all_sprites = all_sprites
        self.soil_sprites = pygame.sprite.Group()

        # graphics
        self.soil_surf = pygame.image.load("./graphics/soil/o.png")

        # requirements
        # if the area is farmable
        self.create_soil_grid()
        # if the soil has been watered
        # if the soil has a plant

    def create_soil_grid(self):
        ground = pygame.image.load("./graphics/world/ground.png")
        h_tiles, v_tiles = ground.get_width() // TILE_SIZE, ground.get_height() // TILE_SIZE
        
        self.grid = [ [[] for col in range(h_tiles)] for row in range(v_tiles) ]
        print(self.grid)