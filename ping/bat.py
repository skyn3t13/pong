import pygame


class Bat(pygame.sprite.Sprite):
    def __init__(self, screen_height, bat_width, bat_height, x, y):
        self.surf = pygame.Surface((bat_width, bat_height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen_height = screen_height
        self.bat_width = bat_width
        self.bat_height = bat_height

    def move_up(self, move_distance):
        if self.rect.y - move_distance > 0:
            self.rect.y -= move_distance

    def move_down(self, move_distance):
        if self.rect.y + move_distance < self.screen_height - self.bat_height:
            self.rect.y += move_distance
