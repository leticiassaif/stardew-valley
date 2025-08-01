import pygame
from settings import *

class Fatigue:
    def __init__(self, player):
        #setup geral
        self.player = player
        self.display_surface = pygame.display.get_surface()
        self.font = self.font = pygame.font.Font("./font/LycheeSoda.ttf", 40)

        #atributos da fadiga
        self.fatigue_estate = False
        self.timer_start = 0
        self.duration = 20000 

    def check_fatigue(self, sky):
        # A verificação da cor é uma forma confiável de saber se a transição para a noite terminou
        is_night = sky.start_color[0] <= sky.end_color[0]
        #ativa a fatiga uma vez por noite
        if is_night and not self.fatigue_estate:
            self.fatigue_estate = True
            self.timer_start = pygame.time.get_ticks()

    def display_warning(self):
        text_surf = self.font.render("You're getting tired...", False, "white")
        text_rect = text_surf.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 20))
        self.display_surface.blit(text_surf, text_rect)

    def reset(self):
        self.fatigue_estate = False

    def update(self, sky, is_raining):
        self.check_fatigue(sky)
        if self.fatigue_estate:
            self.display_warning()
            if pygame.time.get_ticks() - self.timer_start >= self.duration:
                self.player.sleep = True
                if is_raining: self.player.current_energy = int(self.player.maximum_energy * 0.50)
                else: self.player.current_energy = int(self.player.maximum_energy * 0.75)
                