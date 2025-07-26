import pygame
from settings import *

#Parei no 6h08min
class Menu:
    def __init__(self, player, toggle_menu):
        
        #general setup
        self.player = player
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font("./font/LycheeSoda.ttf", 30)
        
        #options
        self.width = 400
        self.space = 10
        self.padding = 8

        #entries
        self.options =  list(self.player.item_inventory.keys()) + list(self.player.seed_inventory.keys())
        self.sell_border =  len(self.player.item_inventory) - 1 #se > buying ou < selling
        self.setup()

    def display_money(self):
        text_surf = self.font.render(f"R${self.player.money}", False, "Black")
        text_rect = text_surf.get_rect(midbottom = (SCREEN_WIDTH / 2,SCREEN_HEIGHT - 20))

        self.display_surface.blit(text_surf,text_rect)

    def setup(self):
        #create the text surf
        self.text_surfs = []
        self.total_height = 0

        for itens in self.options:
            text_surf = self.font.render(itens, False, "black")
            self.text_surfs.append(text_surf)
            self.total_height += text_surf.get_height() + (self.padding*2)
        
        self.total_height += (len(self.text_surfs))*self.space - 1 #se tiver 3 elementos, vai ter 2 espaços
        self.menu_top = (SCREEN_HEIGHT / 2) - (self.total_height /  2)#sempre no meio
        self.main_rect = pygame.Rect((SCREEN_WIDTH/2) - (self.width/2),self.menu_top,self.width,self.total_height)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            self.toggle_menu()

    def update(self): #vai mostrar o menu
        self.input()
        self.display_money()
        pygame.draw.rect(self.display_surface, 'red', self.main_rect)
        # for text_index, text_surf in enumerate(self.text_surfs):
        #     self.display_surface.blit(text_surf, (100,text_index*50))