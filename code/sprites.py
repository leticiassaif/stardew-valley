import pygame
from settings import *

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = layers["main"]):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-self.rect.width*0.2,-self.rect.height*0.75) # w < h

class Water(Generic): #Não precisa de Hitbox
    def __init__(self, pos, frames, groups):
        # animation setup
        self.frames = frames
        self.frame_index = 0

        # sprite setup
        super().__init__(pos = pos,
                         surf = self.frames[self.frame_index],
                         groups = groups, 
                         z = layers["water"])
        
    def animate(self, dt):
        self.frame_index += 5 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self,dt):
        self.animate(dt)

class WildFlower(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy().inlfate(-20,-self.rect.height*0.9)

class Tree(Generic):
    def __init__(self, pos, surf, groups, name):
        super().__init__(pos, surf, groups)

        # #apples
        # self.apples_surf =  pygame.image.load("./graphics/fruit/apple.png")
        # self.apple_pos =apple_pos[name]