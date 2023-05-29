import pygame
import random
import sys
import button

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((500, 500))

# Define the functions for each screen
def main_menu():
    global current_screen
    # Display the main menu and wait for user input
    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Menu Screen")

    background_img = pygame.image.load("BG/main/Halloween.png")
    background_image = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    HW_start_img = pygame.image.load("Button/main_button/start_button_HW-transformed.png").convert_alpha()
    HW_options_img = pygame.image.load("Button/main_button/option_button_HW-transformed.png").convert_alpha()
    HW_score_img = pygame.image.load("Button/main_button/score_button_HW-transformed.png").convert_alpha()

    start_button = button.Button(10, 400, HW_start_img, 0.2)
    options_button = button.Button(170, 400, HW_options_img, 0.2)
    score_button = button.Button(330, 404, HW_score_img, 0.2)

    running = True

    while running:

        for event in pygame.event.get():

            screen.blit(background_image, (0, 0))
            if options_button.draw(screen):
                current_screen = "options"
                options()
            if start_button.draw(screen):
                current_screen = "game"
                play_game()
            if score_button.draw(screen):
                game_started = True

            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    return current_screen



def play_game():
    global ball_speed_x, ball_speed_y

    def ball_movement():
        global ball_speed_x, ball_speed_y

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_speed_y *= -1
        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball_reset()

        if ball.colliderect(user) or ball.colliderect(opponent):
            ball_speed_x *= -1

    def player_movement():
        user.y += user_speed
        if user.top <= 0:
            user.top = 0
        if user.bottom >= SCREEN_HEIGHT:
            user.bottom = SCREEN_HEIGHT

    def opponent_ai():
        if opponent.top < ball.y:
            opponent.top += opponent_speed
        if opponent.bottom > ball.y:
            opponent.bottom -= opponent_speed
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= SCREEN_HEIGHT:
            opponent.bottom = SCREEN_HEIGHT

    def ball_reset():
        global ball_speed_x, ball_speed_y
        ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    pygame.init()
    clock = pygame.time.Clock()

    SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Single player')

    background_img = pygame.image.load("BG/main/Halloween.png")
    background_image = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    ball = pygame.Rect(SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2 - 10, 20, 20)
    user = pygame.Rect(15, SCREEN_HEIGHT / 2 - 40, 15, 80)
    opponent = pygame.Rect(SCREEN_WIDTH - 30, SCREEN_HEIGHT / 2 - 40, 15, 80)

    color = (200, 200, 200)

    ball_speed_x = 4 * random.choice((1, -1))
    ball_speed_y = 4 * random.choice((1, -1))
    user_speed = 0
    opponent_speed = 5

    while running:

        for event in pygame.event.get():

            screen.blit(background_image, (0, 0))

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    user_speed += 5
                if event.key == pygame.K_UP:
                    user_speed -= 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    user_speed -= 5
                if event.key == pygame.K_UP:
                    user_speed += 5

        ball_movement()
        player_movement()
        opponent_ai()

        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, color, user)
        pygame.draw.rect(screen, color, opponent)
        pygame.draw.ellipse(screen, color, ball)
        pygame.draw.aaline(screen, color, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))



        pygame.display.flip()
        clock.tick(60)

def options():
    global current_screen
    # Handle options and wait for user input
    pygame.init()

    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 500

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Options Screen')

    BG = pygame.image.load('BG/option/Halloween_opt.png')
    BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
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

    win_3_button = button.Button(30, 115, win_3_img, 1)
    win_5_button = button.Button(125, 115, win_5_img, 1)
    win_10_button = button.Button(212, 115, win_10_img, 1)
    win_15_button = button.Button(305, 115, win_15_img, 1)
    win_20_button = button.Button(395, 115, win_20_img, 1)
    slow_yes_button = button.Button(168, 213, slow_yes_img, 1)
    slow_no_button = button.Button(262, 213, slow_no_img, 1)
    sp_theme_opt_button = button.Button(50, 312, sp_theme_opt_img, 1)
    fs_theme_opt_button = button.Button(155, 312, fs_theme_opt_img, 1)
    hw_theme_opt_button = button.Button(259, 312, hw_theme_opt_img, 1)
    jg_theme_opt_button = button.Button(361, 312, jg_theme_opt_img, 1)
    back_button = button.Button(165, 400, back_img, 1)
    reset_button = button.Button(270, 400, reset_img, 1)

    run = True
    while run:

        for event in pygame.event.get():
            screen.blit(BG, (0, 0))

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
                BG = pygame.image.load('BG/Space_background.png')
            if fs_theme_opt_button.draw(screen):
                BG = pygame.image.load('BG/Halloween.png')
            if hw_theme_opt_button.draw(screen):
                BG = pygame.image.load('BG/Halloween_opt.png')
            if jg_theme_opt_button.draw(screen):
                BG = pygame.image.load('BG/Jungle_Theme.png')
            if back_button.draw(screen):
                current_screen = "menu"
                main_menu()
            if reset_button.draw(screen):
                print('reset')
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

# Create a variable to track the current screen
current_screen = "menu"

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Use an if-else statement to call the appropriate function based on the current screen
    if current_screen == "menu":
        main_menu()
    elif current_screen == "game":
        play_game()
    elif current_screen == "options":
        options()

    # Update the display
    pygame.display.update()

# Clean up and exit
pygame.quit()
