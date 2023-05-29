import pygame
import button

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Game Screen")

game_started = False

background_img = pygame.image.load("images/Space_background.png")
background_image = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

start_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
score_img = pygame.image.load("images/button_quit.png").convert_alpha()

start_button = button.Button(25, 400, start_img, 1)
options_button = button.Button(230, 400, options_img, 1)
score_button = button.Button(450, 400, score_img, 1)

running = True
while running:

    for event in pygame.event.get():

        screen.blit(background_image, (0,0))

        if game_started == False:
            if start_button.draw(screen):
                game_started = True
            if options_button.draw(screen):
                game_started = True
            if score_button.draw(screen):
                running = False

        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
pygame.quit()
