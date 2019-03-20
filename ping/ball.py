import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.x_speed = -4
        self.y_speed = -10
        self.speed = (self.x_speed, self.y_speed)

    def update(self, *args):
        if self.rect.left < 0:
            self.rect.left = 0
            self.reverse_horizontal_direction()
        elif self.rect.right > 800:
            self.rect.right = 800
            self.reverse_horizontal_direction()
        if self.rect.top <= 0:
            self.rect.top = 0
            self.reverse_vertical_direction()
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.reverse_vertical_direction()

    def reverse_vertical_direction(self):
        self.y_speed = self.y_speed * -1
        self.speed = (self.x_speed, self.y_speed)

    def reverse_horizontal_direction(self):
        self.x_speed = self.x_speed * -1
        self.speed = (self.x_speed, self.y_speed)