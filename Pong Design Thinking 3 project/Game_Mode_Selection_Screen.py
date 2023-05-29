import pygame
import button

pygame.init()

SCREEN_HEIGHT, SCREEN_WIDTH = 600, 600

# create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Mode Selection Screen Test")

game_started = False

# load screen background image
screen_backgroundImg = pygame.image.load("images/FantasyBackground.png")
screen_backgroundImage = pygame.transform.scale(screen_backgroundImg, ((SCREEN_WIDTH, SCREEN_HEIGHT)))

# load button images
selectSingleplayerModeImage = pygame.image.load("button_images/fantasy/fantasy_singleplayer.png").convert_alpha()
selectSingleplayerModeButton = button.Button(150, 100, selectSingleplayerModeImage, 0.4)

selectTwoMultiplayerModeImage = pygame.image.load("button_images/fantasy/fantasy_2player.png").convert_alpha()
selectTwoMultiplayerModeButton = button.Button(150, 200, selectTwoMultiplayerModeImage, 0.4)

selectFourMultiplayerModeImage = pygame.image.load("button_images/fantasy/fantasy_4player.png").convert_alpha()
selectFourMultiplayerModeButton = button.Button(150, 300, selectFourMultiplayerModeImage, 0.4)

selectEndlessModeImage = pygame.image.load("button_images/fantasy/fantasy_endless.png").convert_alpha()
selectEndlessModeButton = button.Button(150, 400, selectEndlessModeImage, 0.4)

running = True
while running:
    for event in pygame.event.get():
        screen.blit(screen_backgroundImage, (0, 0))

        if game_started == False:

            if selectSingleplayerModeButton.draw(screen):
                game_started = True
                print("Singleplayer mode selected")

            if selectTwoMultiplayerModeButton.draw(screen):
                game_started = True
                print("2P Multiplayer selected")

            if selectFourMultiplayerModeButton.draw(screen):
                game_started = True
                print("4P Multiplayer selected")

            if selectEndlessModeButton.draw(screen):
                game_started = True
                print("Endless mode selected")

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
