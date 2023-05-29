import pygame
from pygame.locals import *
pygame.init()


def button(window, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(window, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(window, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(window, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(window, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(window, (100, 100, 100), (x, y, w , h))
    return window.blit(text_render, (x, y))

def start():
    print('Let us start!')

def main():
    width,height = 500,500
    window = pygame.display.set_mode((width,height))

    bg_img = pygame.image.load('BG/Space_background.png')
    bg_img = pygame.transform.scale(bg_img,(width,height))

    b1 = button(window, (40, 30), "Quit")
    b2 = button(window, (40, 30), "Start")

    run = True
    while run:
        window.blit(bg_img,(0,0))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    start()
        pygame.display.update()
    pygame.quit()
main()
