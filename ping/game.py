import pygame
import numpy as np
from pygame.locals import *
from ping.bat import Bat
from ping.ball import Ball
from ping.player import Player
from ping.ai import Ai

class Game:

    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 800
    BAT_WIDTH = 10
    BAT_HEIGHT = 100
    BAT_MOVE = 10
    Y_MIDDLE_SCREEN = SCREEN_HEIGHT / 2
    X_MIDDLE_SCREEN = SCREEN_WIDTH / 2
    RIGHT_BAT_X_POSITION = SCREEN_WIDTH - BAT_WIDTH

    def __init__(self, ball=Ball(Y_MIDDLE_SCREEN, X_MIDDLE_SCREEN)):

        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Game.SCREEN_WIDTH,
                                               Game.SCREEN_HEIGHT))
        self.left_bat = Bat(Game.SCREEN_HEIGHT,
                            Game.BAT_WIDTH,
                            Game.BAT_HEIGHT,
                            0,
                            Game.Y_MIDDLE_SCREEN)
        self.left_player = Player(pygame.K_w, pygame.K_s)
        self.right_bat = Bat(Game.SCREEN_HEIGHT,
                             Game.BAT_WIDTH,
                             Game.BAT_HEIGHT,
                             Game.RIGHT_BAT_X_POSITION,
                             Game.Y_MIDDLE_SCREEN)
        self.right_player = Player(pygame.K_UP, pygame.K_DOWN)
        self.ball = ball           
        self.ball.rect.y = Game.Y_MIDDLE_SCREEN
        self.ball.rect.x = Game.X_MIDDLE_SCREEN
        self.background = pygame.Surface(self.screen.get_size())
        self.score = {"p1": 0, "p2": 0}
        self.robotron3000 = Ai()

    def check_bat_move(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.left_player.key_up]:
            self.left_bat.move_up(Game.BAT_MOVE)
        if keys_pressed[self.left_player.key_down]:
            self.left_bat.move_down(Game.BAT_MOVE)
        if keys_pressed[self.right_player.key_up]:
            self.right_bat.move_up(Game.BAT_MOVE)
        if keys_pressed[self.right_player.key_down]:
            self.right_bat.move_down(Game.BAT_MOVE)

    def check_ball_hits_bat(self):
        if self.ball.rect.colliderect(self.left_bat):
            self.ball.reverse_horizontal_direction()
        if self.ball.rect.colliderect(self.right_bat):
            self.ball.reverse_horizontal_direction()

    def output_data(self):
        output = {"l": self.left_bat.rect.y,
                  "r": self.right_bat.rect.y,
                  "bx": self.ball.rect.x,
                  "by": self.ball.rect.y,
                  "score": self.score}
        return output

    def prepare_data(self, data_hash):
        array = list(data_hash.values())[:4]
        # array.append(data_hash['score']['p1'])
        # array.append(data_hash['score']['p2'])
        numpy_array = np.array(array)
        return numpy_array

    def game_loop(self):
        self.rect = self.screen.get_rect()

        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

            if self.ball.reset:
                self.ball.reset_ball()
            self.screen.fill((0, 0, 0))
            self.clock.tick(60)
            self.ball.rect.move_ip(self.ball.speed)
            self.ball.update(self.score)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.ball.surf, self.ball.rect)
            self.screen.blit(self.left_bat.surf, self.left_bat.rect)
            self.screen.blit(self.right_bat.surf, self.right_bat.rect)
            self.check_bat_move()
            self.check_ball_hits_bat()
            self.robotron3000.send_state(self.prepare_data(self.output_data()))
            # print(self.prepare_data(self.output_data()))
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.game_loop()
