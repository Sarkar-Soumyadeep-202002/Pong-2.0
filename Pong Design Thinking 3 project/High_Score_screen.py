import pygame
import button

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu Screen")

game_started = False

background_img = pygame.image.load("BG/High_score.png")
background_image = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

back_img = pygame.image.load("Button/Options_button/back.png").convert_alpha()
back_button = button.Button(210, 432, back_img, 1)


running = True
while running:

    for event in pygame.event.get():

        screen.blit(background_image, (0, 0))

        if back_button.draw(screen):
            running = False
        
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
