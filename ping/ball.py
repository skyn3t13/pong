import pygame
import random
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, y_middle, x_middle):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((25, 25)) # pylint: disable=too-many-function-args
        self.set_white()
        self.rect = self.surf.get_rect()
        self.speed = 0
        self.set_ball_speed()
        self.y_middle = y_middle
        self.x_middle = x_middle
        self.reset = False
        self.random = 0

    def update(self, score):
        if self.rect.left < 0:
            self.rect.left = 0
            self.stop_ball()
            score["p2"] += 1
            self.set_black()
            self.reset = True

        if self.rect.right > 800:
            self.rect.right = 800
            self.stop_ball()
            score["p1"] += 1
            self.set_black()
            self.reset = True

        if self.rect.top <= 0:
            self.rect.top = 0
            self.reverse_vertical_direction()

        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.reverse_vertical_direction()

    def reverse_vertical_direction(self):
        self.speed = (self.speed[0], self.speed[1] * -1)

    # def reverse_horizontal_direction(self):
        # self.speed = (self.speed[0] * -1, self.speed[1])
        # self.set_random_angle()

    def stop_ball(self):
        self.set_ball_speed(0, 0)

    def set_ball_speed(self, x_speed=10, y_speed=0):
        self.speed = (x_speed, y_speed)

    def reset_ball(self):
        self.set_ball_speed(self.starting_player(), 0)
        self.rect.y = self.y_middle
        self.rect.x = self.x_middle
        self.set_white()
        self.reset = False

    def set_black(self):
        self.surf.fill((0, 0, 0))

    def set_white(self):
        self.surf.fill((255, 255, 255))

    def random_angle(self):
        self.random = (random.randrange(-3, 3))
        return self.random

    def random_y(self):
        return self.speed[1] + self.random_angle()

    def set_random_angle(self):
        speed_y = self.random_y()
        if self.speed[0] < 0:
            self.speed = (((10 - abs(speed_y))), speed_y)
        elif self.speed[0] > 0:
            self.speed = (((10 - abs(speed_y)) * -1), speed_y)

    def angle_limiter(self, x_speed):
        if abs(self.speed[1]) > 8:
            self.speed = (x_speed, 8)

    def starting_player(self):
        number = random.sample([-10, 10], 1)
        return number[0]
