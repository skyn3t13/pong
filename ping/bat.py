import pygame

class Bat:
    def __init__(self, screen_width, screen_height, bat_width, bat_height):
        self.left_bat = pygame.Rect(0,
                                    screen_height / 2 - bat_height / 2,
                                    bat_width,
                                    bat_height)
        self.right_bat = pygame.Rect(screen_width - bat_width,
                                     screen_height / 2 - bat_height / 2,
                                     bat_width,
                                     bat_height)
