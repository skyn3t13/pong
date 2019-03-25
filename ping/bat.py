import pygame


class Bat(pygame.sprite.Sprite):
    def __init__(self, screen_height, bat_width, bat_height, x_pos, y_pos):  # pylint: disable=too-many-arguments
        super(Bat, self).__init__()
        self.surf = pygame.Surface((bat_width, bat_height))  # pylint: disable=too-many-function-args
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.screen_height = screen_height
        self.bat_width = bat_width
        self.bat_height = bat_height

    def move_up(self, move_distance=10):
        if self.rect.y - move_distance > 0:
            self.rect.y -= move_distance

    def move_down(self, move_distance=10):
        if self.rect.y + move_distance < self.screen_height - self.bat_height:
            self.rect.y += move_distance
