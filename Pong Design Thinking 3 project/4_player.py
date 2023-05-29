import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('4 Player Screen')

background_img = pygame.image.load("images/Space_background.png")
background_image = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

ball = pygame.Rect(SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 - 10,20,20)
player_left = pygame.Rect(15, SCREEN_HEIGHT/2 - 40,15,80)
player_right = pygame.Rect(SCREEN_WIDTH - 30, SCREEN_HEIGHT/2 - 40,15,80)
player_up = pygame.Rect(SCREEN_WIDTH/2 - 40, 15, 80,15)
player_down = pygame.Rect(SCREEN_WIDTH/2 - 40, SCREEN_HEIGHT - 30, 80, 15)

color = (200,200,200)

ball_speed_x = 4 * random.choice((1,-1))
ball_speed_y = 4 * random.choice((1,-1))
player_left_speed = 0
player_right_speed = 0
player_up_speed = 0
player_down_speed = 0

def ball_movement():
    global ball_speed_x, ball_speed_y
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y 

    if ball.top <= 0 or  ball.bottom >= SCREEN_HEIGHT:
        # ball_speed_y *= -1
        ball_reset()
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_reset()

    if ball.colliderect(player_left) or ball.colliderect(player_right):
        ball_speed_x *= -1
    if ball.colliderect(player_up) or ball.colliderect(player_down):
        ball_speed_y *= -1

def player_movement():
    player_left.y += player_left_speed
    player_right.y += player_right_speed
    player_up.x += player_up_speed
    player_down.x += player_down_speed

    if player_right.top <= 0:
        player_right.top = 0
    if player_right.bottom >= SCREEN_HEIGHT:
        player_right.bottom = SCREEN_HEIGHT

    if player_left.top <= 0:
        player_left.top = 0
    if player_left.bottom >= SCREEN_HEIGHT:
        player_left.bottom = SCREEN_HEIGHT
    
    if player_up.left <= 0:
        player_up.left = 0
    if player_up.right >= SCREEN_WIDTH:
        player_up.right = SCREEN_WIDTH

    if player_down.left <= 0:
        player_down.left = 0
    if player_down.right >= SCREEN_WIDTH:
        player_down.right = SCREEN_WIDTH

def ball_reset():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))

while running:

    for event in pygame.event.get():

        screen.blit(background_image, (0,0))

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_right_speed += 5
            if event.key == pygame.K_UP:
                player_right_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_right_speed -= 5
            if event.key == pygame.K_UP:
                player_right_speed += 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_left_speed -= 5
            if event.key == pygame.K_s:
                player_left_speed += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_left_speed += 5
            if event.key == pygame.K_s:
                player_left_speed -= 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                player_up_speed -= 5
            if event.key == pygame.K_x:
                player_up_speed += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                player_up_speed += 5
            if event.key == pygame.K_x:
                player_up_speed -= 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                player_down_speed -= 5
            if event.key == pygame.K_p:
                player_down_speed += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_o:
                player_down_speed += 5
            if event.key == pygame.K_p:
                player_down_speed -= 5


    ball_movement()
    player_movement()

    screen.blit(background_image, (0,0))
    pygame.draw.rect(screen, color, player_left)
    pygame.draw.rect(screen, color, player_right)
    pygame.draw.ellipse(screen, color, ball)
    pygame.draw.rect(screen, color, player_up)
    pygame.draw.rect(screen, color, player_down)
    pygame.draw.aaline(screen, color, (SCREEN_WIDTH/2,0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    pygame.display.flip()
    clock.tick(60)
