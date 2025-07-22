import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,500)) #width = 800, height = 400
pygame.display.set_caption("Leticia's Dress Up")
clock = pygame.time.Clock()
running = True

#fonte
font = pygame.font.Font(None, 50) #font type, font size -- font/*nome*.ttf

#surfaces
test_surface = pygame.Surface((100,200))
# para imagem : pygame.image.load(pasta/nome da imagem)
test_surface.fill("red")
text_surface = font.render("My game", False, "Green") #text, AA, color

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # if running:
        # if pygame.mouse.get_pressed()[0] and new_press: toggle buttons
        #     new_press = False

        # if not pygame.mouse.get_pressed()[0] and not new_press:
        #     new_press = True
        
    screen.blit(test_surface,(200,100)) #surface, position
    screen.blit(text_surface,(300,50))

    pygame.display.update()
    clock.tick(60) # 60fps no máximo
    # else running = False