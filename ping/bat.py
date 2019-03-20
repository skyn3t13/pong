import pygame


class Bat(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, bat_width, bat_height, x, y):
        self.surf = pygame.Surface((bat_width, bat_height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y



    def move_up(self, side, screen_height, bat_height, move_distance):
        bat = self.left_bat if side == 'left' else self.right_bat
        if bat.y - move_distance > 0:
            bat.y -= move_distance

    def move_down(self, side, screen_height, bat_height, move_distance):
        bat = self.left_bat if side == 'left' else self.right_bat
        if bat.y + move_distance < screen_height - bat_height:
            bat.y += move_distance
