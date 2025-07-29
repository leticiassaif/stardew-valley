import pygame, sys
from settings import *
from timer import Timer # type: ignore

class Menu:
    def __init__(self, player, toggle_menu):
        
        # general setup
        self.player = player
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font("./font/LycheeSoda.ttf", 30)
        
        # options
        self.width = 400
        self.space = 10
        self.padding = 8

        # entries
        self.options =  list(self.player.item_inventory.keys()) + list(self.player.seed_inventory.keys())
        self.sell_border =  len(self.player.item_inventory) - 1 #se > buying ou < selling
        self.setup()

        # movement
        self.index = 0 # movimentação da loja
        self.timer = Timer(200) # 200ms para mudar de item para não ficar rápido demais
        
    def display_money(self):
        text_surf = self.font.render(f"R${self.player.money}", False, "Black")
        text_rect = text_surf.get_rect(midbottom = (SCREEN_WIDTH / 2,SCREEN_HEIGHT - 20))

        pygame.draw.rect(self.display_surface, "White",text_rect.inflate(10,10),0,4) # 4 deixa o rect redondo
        self.display_surface.blit(text_surf,text_rect)

    def setup(self):
        # create the text surf
        self.text_surfs = []
        self.total_height = 0

        for itens in self.options:
            text_surf = self.font.render(itens, False, "black")
            self.text_surfs.append(text_surf)
            self.total_height += text_surf.get_height() + (self.padding*2)

        self.total_height += (len(self.text_surfs) - 1) * self.space #se tiver 3 elementos, vai ter 2 espaços
        self.menu_top = SCREEN_HEIGHT / 2 - self.total_height /  2 #sempre no meio
        self.main_rect = pygame.Rect(SCREEN_WIDTH/2 - self.width/2,self.menu_top,self.width,self.total_height)

        #buy/sell text surfs
        self.buy_text = self.font.render("Buy", False, "Black")
        self.sell_text = self.font.render("Sell", False, "Black")

    def input(self):
        keys = pygame.key.get_pressed()
        self.timer.update()

        if keys[pygame.K_ESCAPE]:
            self.toggle_menu()

        if not self.timer.active:
            if keys[pygame.K_UP]:
                self.index -= 1
                self.timer.activate()

            if keys[pygame.K_DOWN]:
                self.index += 1
                self.timer.activate()

            if keys[pygame.K_SPACE]:
                self.timer.activate()

                #get the item
                current_item = self.options[self.index]

                #sell
                if self.index <= self.sell_border:
                    if self.player.item_inventory[current_item] > 0:
                        self.player.item_inventory[current_item] -= 1
                        self.player.money += sale_prices[current_item]
                #buy
                else:
                    seed_price = purchase_prices[current_item]
                    if self.player.money >= seed_price:
                        self.player.seed_inventory[current_item] += 1
                        self.player.money -= purchase_prices[current_item]


        #clamp value
        if self.index < 0:
            self.index = len(self.text_surfs) - 1
        elif self.index > len(self.text_surfs)-1:
            self.index = 0

    def show_entry(self, text_surf, amount, top, selected):
       
        #background
        bg_rect  = pygame.Rect(self.main_rect.left,top,self.width,text_surf.get_height() + (self.padding*2))
        pygame.draw.rect(self.display_surface, "White", bg_rect,0,4)

        #text // direita
        text_rect = text_surf.get_rect(midleft = (self.main_rect.left + 20, bg_rect.centery))
        self.display_surface.blit(text_surf, text_rect)

        #amount // esquerda
        amount_surf = self.font.render(str(amount), False, "Black")
        amount_rect = amount_surf.get_rect(midright = (self.main_rect.right - 20, bg_rect.centery))
        self.display_surface.blit(amount_surf, amount_rect)

        #selected
        if selected:
            pygame.draw.rect(self.display_surface, "Black", bg_rect, 4, 4)
            if self.index <= self.sell_border: #sell
                pos_rect = self.sell_text.get_rect(midleft = (self.main_rect.left + 180, bg_rect.centery))
                self.display_surface.blit(self.sell_text, pos_rect)
            else: #buy
                 pos_rect = self.buy_text.get_rect(midleft = (self.main_rect.left + 180, bg_rect.centery))
                 self.display_surface.blit(self.buy_text, pos_rect)
    
    def update(self): #vai mostrar o menu
        self.input()
        self.display_money()
        # pygame.draw.rect(self.display_surface, 'red', self.main_rect) # mostra os espaços do menu
        for text_index, text_surf in enumerate(self.text_surfs): 
            # 0 = 1 rect; 1 = 2 rect com padding de distancia de rect 1,..., // #top é o topo de cada rect
            top = self.main_rect.top + text_index * ( text_surf.get_height() + (self.padding * 2) + self.space)
            amount_list = list(self.player.item_inventory.values()) + list(self.player.seed_inventory.values())
            amount = amount_list[text_index]
            self.show_entry(text_surf, amount, top, self.index == text_index)

class Pause(Menu):
    def setup(self):
        self.pause_surfs = []
        self.total_height = 0

        self.pause_options = ["resume", "options", "quit"]

        for i in self.pause_options:
            pause_surf = self.font.render(i, False, "black")
            self.pause_surfs.append(pause_surf)
            self.total_height += pause_surf.get_height() + (self.padding*2)

        self.total_height += (len(self.pause_surfs) - 1) * self.space #se tiver 3 elementos, vai ter 2 espaços
        self.menu_top = SCREEN_HEIGHT / 2 - self.total_height /  2 #sempre no meio
        self.main_rect = pygame.Rect(SCREEN_WIDTH/2 - self.width/2,self.menu_top,self.width,self.total_height)

    def input(self):
        keys = pygame.key.get_pressed()
        self.timer.update()

        # if keys[pygame.K_ESCAPE]:
        #     self.toggle_menu()

        if not self.timer.active:
            if keys[pygame.K_UP]:
                self.index -= 1
                self.timer.activate()

            if keys[pygame.K_DOWN]:
                self.index += 1
                self.timer.activate()

        if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
            self.timer.activate()
            selected_option = self.pause_options[self.index]
            if selected_option == "resume":
                self.toggle_menu()
            elif selected_option == "quit":
                pygame.quit()
                sys.exit()
            # else:

        # Clamp value
        if self.index < 0:
            self.index = len(self.pause_surfs) - 1
        elif self.index > len(self.pause_surfs) - 1:
            self.index = 0

    def update(self):
        self.input()
        for pause_index, pause_surf in enumerate(self.pause_surfs): 
            top = self.main_rect.top + pause_index * ( pause_surf.get_height() + (self.padding * 2) + self.space)
            background_rect = pygame.Rect(self.main_rect.left, top, self.width, pause_surf.get_height() + (self.padding*2))
            pygame.draw.rect(self.display_surface, "White", background_rect, 0, 4)
            text_rect = pause_surf.get_rect(midleft=(self.main_rect.left + 20, background_rect.centery))
            self.display_surface.blit(pause_surf, text_rect)
            if self.index == pause_index:
                pygame.draw.rect(self.display_surface, "Black", background_rect, 4, 4)
