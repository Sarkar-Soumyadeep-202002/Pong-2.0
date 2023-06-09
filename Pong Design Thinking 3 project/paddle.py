import pygame
import random


class Paddle:
    """ A class to manage the paddles """

    def __init__(self, ai_game, position):
        """ Create a paddle """
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # self.rect = pygame.Rect(0, 0, self.settings.paddle_width, self.settings.paddle_height)
        # self.image = pygame.image.load("Assets/SpacePaddle.png")
        self.image = pygame.image.load("Assets/HalloweenPaddle.png")
        # self.image = pygame.image.load("Assets/green_worm.png")
        # self.image = pygame.image.load("Assets/Mage_Paddle.png")
        self.image = pygame.transform.scale(self.image, self.settings.paddle_size)

        self.rect = self.image.get_rect()
        self.position = position

        self.number_lives = self.settings.number_lives

        self.reset_paddle()

    def reset_paddle(self):
        if self.position == "left":
            self.rect.left = self.settings.separetion
        else:
            self.rect.right = self.settings.screen_width - self.settings.separetion
        self.rect.centery = self.screen_rect.centery

        self.move_down = False
        self.move_up = False

    def update_paddle(self):
        """ Update the paddle and draw it on the screen """
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.paddle_speed
        elif self.move_up and self.rect.top > 0:
            self.rect.y -= self.settings.paddle_speed

        self.screen.blit(self.image, self.rect)
