import pygame
from settings import *

class Overlay:
    def __init__(self, player):

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # import
        overlay_path = "./graphics/overlay/"
        self.tools_surf = {tool: pygame.image.load(f"{overlay_path}{tool}.png").convert_alpha() for tool in player.tools}
        self.seeds_surf = {seed: pygame.image.load(f"{overlay_path}{seed}.png").convert_alpha() for seed in player.seeds}
        print(self.tools_surf)
        print(self.seeds_surf)