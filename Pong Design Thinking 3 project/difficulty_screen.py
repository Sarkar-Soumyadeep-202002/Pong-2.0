import pygame
import button

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Difficulty Screen")

#dif_bg = pygame.image.load('BG/difficulty/halloween_diff.png')
dif_bg = pygame.image.load('BG/difficulty/jungle_diff.png')
#dif_bg = pygame.image.load('BG/difficulty/space_diff.png')
#dif_bg = pygame.image.load('BG/difficulty/fs_diff.png')

dif_bg_img = pygame.transform.scale(dif_bg, (SCREEN_WIDTH,SCREEN_HEIGHT))

hw_easy_img = pygame.image.load('Button/difficulty_button/easy_button.png')
easy_button = button.Button(200, 220, hw_easy_img, 1)
hw_normal_img = pygame.image.load('Button/difficulty_button/normal.png')
normal_button = button.Button(200, 260, hw_normal_img, 1)
hw_hardcore = pygame.image.load('Button/difficulty_button/hardcore_button.png')
hardcore_button = button.Button(200, 300, hw_hardcore, 1)

running = True
dif_page = True

while running:

    for event in pygame.event.get():
        screen.blit(dif_bg_img,(0,0))

        if dif_page ==True:
            if easy_button.draw(screen):
                print('easy')
            if normal_button.draw(screen):
                print('normal')
            if hardcore_button.draw(screen):
                print('hardcore')

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()