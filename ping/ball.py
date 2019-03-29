import random
import pygame


class Ball(pygame.sprite.Sprite):  #pylint: disable=too-many-instance-attributes, too-many-public-methods

    SPEED_LIMIT = 8

    def __init__(self, x_middle, y_middle):
        super(Ball, self).__init__()
        self.number = 25
        self.surf = pygame.Surface((self.number, self.number))  # pylint: disable=too-many-function-args
        self.set_white()
        self.rect = self.surf.get_rect()
        self.speed = 0
        self.set_ball_speed()
        self.y_middle = y_middle
        self.x_middle = x_middle
        self.reset = False
        self.random = 0
        self.colour = [0, 0, 0]
        self.three_d_turned_on = False

    def update(self, score):
        self.change_colour()
        if self.three_d_turned_on:
            self.ball_3d_controller()
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

    def turn_3d_on(self):
        self.three_d_turned_on = True

    def reverse_vertical_direction(self):
        self.speed = (self.speed[0], self.speed[1] * -1)

    def stop_ball(self):
        self.set_ball_speed(0, 0)

    def set_ball_speed(self, x_speed=10, y_speed=0):
        self.speed = (x_speed, y_speed)

    def reset_ball(self):
        self.set_ball_speed(self.starting_player(), 0)
        self.number = 25
        self.adjust_ball_size()
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

    def starting_player(self):
        return random.choice([-10, 10])

    def change_colour(self):
        self.Rand(0, 255, 3)
        self.surf.fill((self.colour))

    def ball_3d_controller(self):
        self.ball_size_protector()
        if self.checks_if_positive(self.speed[0]):
            self.ball_rightward_adjustment()
        else:
            self.ball_leftward_adjustment()

    def ball_rightward_adjustment(self):
        if self.rect.x < 380:
            if self.divisible_by_two():
                self.increment_number()
                self.adjust_ball_size()
        elif self.rect.x > 420:
            if self.divisible_by_two():
                self.decrease_number()
                self.adjust_ball_size()

    def ball_leftward_adjustment(self):
        if self.rect.x < 380:
            if self.divisible_by_two():
                self.decrease_number()
                self.adjust_ball_size()
        elif self.rect.x > 420:
            if self.divisible_by_two():
                self.increment_number()
                self.adjust_ball_size()

    def increment_number(self):
        self.number += 1

    def decrease_number(self):
        self.number -= 1

    def divisible_by_two(self):
        return bool(self.rect.x % 2 == 0)

    def adjust_ball_size(self):
        self.surf = pygame.transform.scale(self.surf, (self.number, self.number))

    def ball_size_protector(self):
        if self.number < 25:
            self.number = 25
        if self.number > 75:
            self.number = 75
        self.adjust_ball_size()

    def Rand(self, start, end, num):  #pylint: disable=invalid-name
        self.colour = []
        for j in range(num):  #pylint: disable=unused-variable
            self.colour.append(random.randint(start, end))
        return self.colour

    def random_y(self):
        return self.speed[1] + self.random_angle()

    def set_random_angle(self):
        speed_y = self.random_y()
        if not self.checks_if_positive(self.speed[0]):
            self.speed = (((10 - abs(speed_y))), speed_y)
        else:
            self.speed = (((10 - abs(speed_y)) * -1), speed_y)

    def angle_limiter(self, x_speed):
        if abs(self.speed[1]) > self.SPEED_LIMIT:
            self.speed = (x_speed, self.SPEED_LIMIT)

    def checks_if_positive(self, value):
        return bool(value > 0)
