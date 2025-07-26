import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("Garden")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update() 

if __name__ == "__main__":
    game = Game()
    game.run()

# #fonte
# font = pygame.font.Font(None, 50) #font type, font size -- font/*nome*.ttf
# screen.blit(test_surface,(200,100)) #surface, position
# screen.blit(text_surface,(300,50))


# clock.tick(60) # 60fps no máximo
# # else running = False

# #surfaces
# test_surface = pygame.Surface((100,200))
# # para imagem : pygame.image.load(pasta/nome da imagem)
# test_surface.fill("red")
# text_surface = font.render("My game", False, "Green") #text, AA, color

# #MOSTRAR HITBOX é em  Level class CameraGroup(pygame.sprite.Group):'