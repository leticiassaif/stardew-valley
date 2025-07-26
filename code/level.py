import pygame
from settings import *
from player import Player
from overlay import Overlay
from sprites import Generic, Water, WildFlower, Tree, Interaction, Particle
from pytmx.util_pygame import load_pygame
from support import *
from transition import Transition
from soil import SoilLayer
from sky import Rain, Sky
from random import randint
from menu import Menu



class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = CameraGroup() # draw & update all sprites in game
        self.collision_sprites = pygame.sprite.Group()
        self.tree_sprites = pygame.sprite.Group()
        self.interaction_sprites = pygame.sprite.Group()

        self.soil_layer = SoilLayer(self.all_sprites, self.collision_sprites)
        self.setup()
        self.overlay = Overlay(self.player)
        self.transition = Transition(self.reset, self.player)

        #sky
        self.rain = Rain(self.all_sprites)
        self.raining = randint(0,10) > 7 #ON/OFF da chuva, ta randomizando o  True  False
        self.soil_layer.raining = self.raining
        self.sky = Sky()

        #shop
        self.menu = Menu(self.player, self.toggle_shop)
        self.shop_active = False #ON/OFF menu do shop

        #music
        self.music = pygame.mixer.Sound("./audio/music.mp3")
        self.music.play(loops = -1)
        self.music.set_volume(0.05)
        self.success = pygame.mixer.Sound("./audio/success.wav")
        self.success.set_volume(0.1)

    def setup(self):
        tmx_data = load_pygame("./data/map.tmx")

        # house
        for layer in ["HouseFloor", "HouseFurnitureBottom"]:
            for x,y,surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, layers["house bottom"])

        for layer in ["HouseWalls", "HouseFurnitureTop"]:
            for x,y,surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites) # layer -> main (default) if not specified

        # fence
        for x,y,surf in tmx_data.get_layer_by_name("Fence").tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        # water
        water_frames = import_folder("./graphics/water")
        for x,y,surf in tmx_data.get_layer_by_name("Water").tiles():
            Water((x * TILE_SIZE, y * TILE_SIZE), water_frames, self.all_sprites)

        # tree
        for obj in tmx_data.get_layer_by_name("Trees"):
            Tree(
                pos = (obj.x, obj.y), 
                surf = obj.image, 
                groups = [self.all_sprites, self.collision_sprites, self.tree_sprites], 
                name = obj.name,
                player_add = self.player_add)

        # wildflowers
        for obj in tmx_data.get_layer_by_name("Decoration"):
            WildFlower((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])

        #collision tiles
        for x, y, surf in tmx_data.get_layer_by_name('Collision').tiles():
            Generic((x*TILE_SIZE,y*TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), self.collision_sprites) #se fizer [self.all_sprites, self.collision_sprites] ele vai mostrar no jogo a "hitbox" da colisão

        # Player
        for obj in tmx_data.get_layer_by_name("Player"):
            if obj.name == "Start":
                self.player = Player( #pos, group
                    pos =(obj.x,obj.y), 
                    group = self.all_sprites, 
                    collision_sprites = self.collision_sprites,
                    tree_sprites = self.tree_sprites,
                    interaction = self.interaction_sprites,
                    soil_layer = self.soil_layer,
                    toggle_shop = self.toggle_shop) 
            
            if obj.name == "Bed":
                Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name) #Area de interação
            
            if obj.name == "Trader":
                Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)

        Generic(
            pos = (0,0),
            surf = pygame.image.load("./graphics/world/ground.png").convert_alpha(), 
            groups = self.all_sprites,
            z = layers["ground"])

    def player_add(self, item):
        # O += random, foi add própria. Assim fica mais parecido com Stardew Valley
        if item == "wood":
            self.player.item_inventory[item] += randint(1,3)
        else: 
            self.player.item_inventory[item] += 1
        self.success.play()

    def toggle_shop(self):

        self.shop_active = not self.shop_active

    def reset(self): # level -> transition -> reset -> level
        # plants
        self.soil_layer.update_plants()

        # soil
        self.soil_layer.remove_water()
        self.raining = randint(0,10) > 7
        self.soil_layer.raining = self.raining
        if self.raining:
            self.soil_layer.water_all()

        # apples on the trees
        for tree in self.tree_sprites.sprites():
            for apple in tree.apple_sprites.sprites():
                apple.kill()
            tree.create_fruit()

        #sky
        self.sky.start_color = [255,255,255]

    def plant_collision(self):
        if self.soil_layer.plant_sprites:
            for plant in self.soil_layer.plant_sprites.sprites():
                if plant.harvestable and plant.rect.colliderect(self.player.hitbox):
                    self.player_add(plant.plant_type)
                    plant.kill()
                    Particle(plant.rect.topleft, plant.image, self.all_sprites, layers["main"])
                    self.soil_layer.grid[plant.rect.centery // TILE_SIZE][plant.rect.centerx // TILE_SIZE].remove("P")

    def run(self, dt):
        
        #Drawing logic
        self.display_surface.fill("black")
        self.all_sprites.custom_draw(self.player)
        
        #updates
        if self.shop_active:
            self.menu.update()
        else:
            self.all_sprites.update(dt)
            self.plant_collision()
    
        ##Clima
        self.overlay.display()
        #rain
        if self.raining and not self.shop_active:
            self.rain.update()
        #daytime:
        self.sky.display(dt)

        #transition overlay
        if self.player.sleep:
            self.transition.play()
            
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer_pos in layers.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer_pos:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)

                    # #MOSTRAR HITBOX
                    # if sprite == player:
                    #     pygame.draw.rect(self.display_surface,'red',offset_rect,5) #player rectangle 
                    #     hitbox_rect = player.hitbox.copy()
                    #     hitbox_rect.center = offset_rect.center
                    #     pygame.draw.rect(self.display_surface,'green', hitbox_rect, 5) #collision hitbox
                    #     target_pos = offset_rect.center + player_tool_offset[player.status.split('_')[0]] 
                    #     pygame.draw.circle(self.display_surface,'blue',target_pos,5) #Target position for tool use