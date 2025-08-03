import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self): # inicialização do jogo
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("Titico's Garden")
        icon = pygame.image.load("./graphics/icon.png")
        self.font = pygame.font.Font("./font/LycheeSoda.ttf", 40)
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.game_start = False
        self.level = Level()
        
    def run(self): # loop do jogo
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.game_start = True
                        
            start_menu = pygame.image.load("./graphics/open_menu.jpg")
            play_instr = self.font.render("Press RETURN to start", False, "white")
            play_rect = play_instr.get_rect(center = (SCREEN_WIDTH//2, 400))

            if not self.game_start:
                self.screen.blit(start_menu, (0,0))
                self.screen.blit(play_instr, play_rect)
            dt = self.clock.tick() / 1000
            if self.game_start:
                self.level.run(dt)
            pygame.display.update() 

if __name__ == "__main__":
    game = Game()
    game.run()

# #MOSTRAR HITBOX é em  Level class CameraGroup(pygame.sprite.Group):'