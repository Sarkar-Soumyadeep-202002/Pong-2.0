import pygame
import button_02

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Game Screen")

game_started = False
game_options = False

background_img = pygame.image.load("BG/Halloween.png")
background_image = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

pong_title_img = pygame.image.load("BG/pong_title.png")
HW_start_img = pygame.image.load("Button/main_button/start_button_HW-transformed.png").convert_alpha()
HW_options_img = pygame.image.load("Button/main_button/option_button_HW-transformed.png").convert_alpha()
HW_score_img = pygame.image.load("Button/main_button/score_button_HW-transformed.png").convert_alpha()


start_button = button_02.Button(10, 400, HW_start_img, 0.2)
options_button = button_02.Button(170, 400, HW_options_img, 0.2)
score_button = button_02.Button(330, 404, HW_score_img, 0.2)

running = True
while running:

    for event in pygame.event.get():

        screen.blit(background_image, (0, 0))

        if game_options == False:
            if start_button.draw(screen):
                game_started = True
            if options_button.draw(screen):
                game_options = True
            if score_button.draw(screen):
                game_started = True

        if game_options == True:
            background_img = pygame.image.load('BG/Halloween_opt.png')
            win_3_img = pygame.image.load('Button/Options_button/win_3.png')
            win_5_img = pygame.image.load('Button/Options_button/win_5.png')
            win_10_img = pygame.image.load('Button/Options_button/win_10.png')
            win_15_img = pygame.image.load('Button/Options_button/win_15.png')
            win_20_img = pygame.image.load('Button/Options_button/win_20.png')
            slow_yes_img = pygame.image.load('Button/Options_button/slow_yes.png')
            slow_no_img = pygame.image.load('Button/Options_button/slow_no.png')
            sp_theme_opt_img = pygame.image.load('Button/Options_button/theme_opt_sp.png')
            fs_theme_opt_img = pygame.image.load('Button/Options_button/theme_opt_fs.png')
            hw_theme_opt_img = pygame.image.load('Button/Options_button/theme_opt_hw.png')
            jg_theme_opt_img = pygame.image.load('Button/Options_button/theme_opt_jg.png')
            back_img = pygame.image.load('Button/Options_button/back.png')
            reset_img = pygame.image.load('Button/Options_button/reset.png')

            win_3_button = button_02.Button(30, 115, win_3_img, 1)
            win_5_button = button_02.Button(125, 115, win_5_img, 1)
            win_10_button = button_02.Button(212, 115, win_10_img, 1)
            win_15_button = button_02.Button(305, 115, win_15_img, 1)
            win_20_button = button_02.Button(395, 115, win_20_img, 1)
            slow_yes_button = button_02.Button(168, 213, slow_yes_img, 1)
            slow_no_button = button_02.Button(262, 213, slow_no_img, 1)
            sp_theme_opt_button = button_02.Button(50, 312, sp_theme_opt_img, 1)
            fs_theme_opt_button = button_02.Button(155, 312, fs_theme_opt_img, 1)
            hw_theme_opt_button = button_02.Button(259, 312, hw_theme_opt_img, 1)
            jg_theme_opt_button = button_02.Button(361, 312, jg_theme_opt_img, 1)
            back_button = button_02.Button(165, 400, back_img, 1)
            reset_button = button_02.Button(270, 400, reset_img, 1)

            for event in pygame.event.get():
                screen.blit(background_img, (0, 0))

                if win_3_button.draw(screen):
                    print('score 3 to win!')
                if win_5_button.draw(screen):
                    print('score 5 to win!')
                if win_10_button.draw(screen):
                    print('score 10 to win!')
                if win_15_button.draw(screen):
                    print('score 15 to win!')
                if win_20_button.draw(screen):
                    print('score 20 to win!')
                if slow_yes_button.draw(screen):
                    print('slow the ball')
                if slow_no_button.draw(screen):
                    print('dont slow the ball')
                if sp_theme_opt_button.draw(screen):
                    background_img = pygame.image.load('BG/Space_background.png')
                if fs_theme_opt_button.draw(screen):
                    background_img = pygame.image.load('BG/Halloween.png')
                if hw_theme_opt_button.draw(screen):
                    background_img = pygame.image.load('BG/Halloween_opt.png')
                if jg_theme_opt_button.draw(screen):
                    background_img = pygame.image.load('BG/Jungle_Theme.png')
                if back_button.draw(screen):
                    print('back')
                if reset_button.draw(screen):
                    print('reset')

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()