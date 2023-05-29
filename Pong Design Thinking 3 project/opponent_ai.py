import pygame, sys, random

def ball_movement():
    global ball_speed_x, ball_speed_y
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y 

    if ball.top <= 0 or  ball.bottom >= SCREEN_HEIGHT:
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
    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Single player')

background_img = pygame.image.load("images/Space_background.png")
background_image = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

ball = pygame.Rect(SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 - 10,20,20)
user = pygame.Rect(15, SCREEN_HEIGHT/2 - 40,15,80)
opponent = pygame.Rect(SCREEN_WIDTH - 30, SCREEN_HEIGHT/2 - 40,15,80)

color = (200,200,200)

ball_speed_x = 4 * random.choice((1,-1))
ball_speed_y = 4 * random.choice((1,-1))
user_speed = 0
opponent_speed = 5

while running:

    for event in pygame.event.get():

        screen.blit(background_image, (0,0))

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

    screen.blit(background_image, (0,0))
    pygame.draw.rect(screen, color, user)
    pygame.draw.rect(screen, color, opponent)
    pygame.draw.ellipse(screen, color, ball)
    pygame.draw.aaline(screen, color, (SCREEN_WIDTH/2,0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    pygame.display.flip()
    clock.tick(60)
