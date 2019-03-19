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

    def move_up(self, side, screen_height, bat_height, move_distance):
        bat = self.left_bat if side == 'left' else self.right_bat
        if bat.y - move_distance > 0:
            bat.y -= move_distance

    def move_down(self, side, screen_height, bat_height, move_distance):
        bat = self.left_bat if side == 'left' else self.right_bat
        if bat.y + move_distance < screen_height - bat_height:
            bat.y += move_distance
