import pygame


class Settings:
    """ A class to manage the settings game """
    
    def __init__(self):
        # Screen settings
        self.screen_width = 500
        self.screen_height = 500
        self.screen_size = (self.screen_width, self.screen_height)

        # Ball settings
        self.ball_size = (30,30)
        self.ball_rate = 1.05

        # Paddle settings
        self.paddle_size = (30, 100)
        self.paddle_width = 15
        self.paddle_height = 100
        self.paddle_color = {"right": (155,155,155), "left": (155,155,155)}
        self.paddle_rate = 1.05
        self.number_lives = 5

        self.separetion = 15
        self.text_color = (255,255,255)
        self.FPS = 60

        self.reset_settings()

    def reset_settings(self):
        """ Reset the unconstant settings """
        self.ball_speed = 6
        self.paddle_speed = 6
