import random
import pygame  # pylint: disable=wildcard-import,ungrouped-imports
import numpy as np
from pygame.locals import *  # pylint: disable=wildcard-import
from ping.bat import Bat
from ping.ball import Ball
from ping.player import Player
from ping.ai import Ai


class Game:  # pylint: disable=too-many-instance-attributes

    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 800
    BAT_WIDTH = 10
    BAT_HEIGHT = 100
    BAT_MOVE = 10
    Y_MIDDLE_SCREEN = SCREEN_HEIGHT / 2
    X_MIDDLE_SCREEN = SCREEN_WIDTH / 2
    RIGHT_BAT_X_POSITION = SCREEN_WIDTH - BAT_WIDTH
    NPC_ON_COLOUR = [0, 255, 0]
    NPC_OFF_COLOUR = [255, 0, 0]
    ANGLE_ON_COLOUR = [0, 128, 128]
    ANGLE_OFF_COLOUR = [0, 0, 128]

    def __init__(self, ball=Ball(Y_MIDDLE_SCREEN, X_MIDDLE_SCREEN)):

        pygame.init()  # pylint: disable=E1101
        self.font = pygame.font.SysFont("monospace", 35)
        self.npc_font = pygame.font.SysFont('Impact', 30)
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Game.SCREEN_WIDTH,
                                               Game.SCREEN_HEIGHT))
        self.left_bat = Bat(Game.SCREEN_HEIGHT,
                            Game.BAT_WIDTH,
                            Game.BAT_HEIGHT,
                            0,
                            Game.Y_MIDDLE_SCREEN)
        self.left_player = Player(pygame.K_w, pygame.K_s)  # pylint: disable=no-member
        self.right_bat = Bat(Game.SCREEN_HEIGHT,  # pylint: disable=no-member
                             Game.BAT_WIDTH,
                             Game.BAT_HEIGHT,
                             Game.RIGHT_BAT_X_POSITION,
                             Game.Y_MIDDLE_SCREEN)
        self.right_player = Player(pygame.K_UP, pygame.K_DOWN)  # pylint: disable=no-member
        self.npc_controller = Player(pygame.K_n, pygame.K_m)
        self.angle_controller = Player(pygame.K_a, pygame.K_z)
        self.npc_on = False
        self.ball_angles_on = False
        self.ball = ball
        self.ball.rect.y = Game.Y_MIDDLE_SCREEN
        self.ball.rect.x = Game.X_MIDDLE_SCREEN
        self.background = pygame.Surface(self.screen.get_size())  # pylint: disable=too-many-function-args
        self.games = 1
        self.epsilon = 1
        self.old_score = {"p1": 0, "p2": 0}
        self.score = {"p1": 0, "p2": 0}
        self.rect = self.rect = self.screen.get_rect()
        self.robotron3000 = Ai(self)
        self.level = 1

    def check_bat_move(self):
        keys_pressed = pygame.key.get_pressed()
        if not self.npc_on:
            if keys_pressed[self.left_player.key_up]:
                self.left_bat.move_up(Game.BAT_MOVE)
            if keys_pressed[self.left_player.key_down]:
                self.left_bat.move_down(Game.BAT_MOVE)
        if keys_pressed[self.right_player.key_up]:
            self.right_bat.move_up(Game.BAT_MOVE)
        if keys_pressed[self.right_player.key_down]:
            self.right_bat.move_down(Game.BAT_MOVE)

    def turn_angles_on_or_off(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.angle_controller.key_up]:
            self.ball_angles_on = True
        if keys_pressed[self.angle_controller.key_down]:
            self.ball_angles_on = False

    def check_if_ball_angles_on(self):
        if self.ball_angles_on:
            self.check_ball_hits_bat_angles()
        else:
            self.check_ball_hits_bat_no_angles()

    def check_ball_hits_bat_angles(self):
        if self.ball.rect.colliderect(self.left_bat):
            self.ball.rect.x = 20
            self.ball.set_random_angle()
            self.ball.angle_limiter(2)
        if self.ball.rect.colliderect(self.right_bat):
            self.ball.rect.x = 760
            self.ball.set_random_angle()
            self.ball.angle_limiter(-2)

    def check_ball_hits_bat_no_angles(self):
        if self.ball.rect.colliderect(self.left_bat):
            self.ball.rect.x = 11
            self.ball.set_random_angle()
            self.ball.angle_limiter(2)

        if self.ball.rect.colliderect(self.right_bat):
            self.ball.rect.x = 764
            self.ball.set_random_angle()
            self.ball.angle_limiter(-2)

    def turns_on_ball_3d(self):
        if self.ball.rect.colliderect(self.right_bat):
            self.ball.turn_3d_on()
        if self.ball.rect.colliderect(self.left_bat):
            self.ball.turn_3d_on()


    def turn_npc_on_or_off(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.npc_controller.key_up]:
            self.npc_on = True
        if keys_pressed[self.npc_controller.key_down]:
            self.npc_on = False

    def moves_npc_player(self):
        chance = random.randint(1, 9999)
        if chance > 3450:
            if self.left_bat.rect.y > self.ball.rect.y:
                self.left_bat.move_up(Game.BAT_MOVE)
            if self.left_bat.rect.y < self.ball.rect.y:
                self.left_bat.move_down(Game.BAT_MOVE)


    def print_npc_status(self):
        if self.npc_on:
            return self.npc_font.render(str('NPC: On'), False, Game.NPC_ON_COLOUR, (0, 0, 0))
        return self.npc_font.render(str('NPC: Off'), False, Game.NPC_OFF_COLOUR, (0, 0, 0))

    def print_angle_status(self):
        if self.ball_angles_on:
            return self.npc_font.render(str('Angles On'), False, Game.ANGLE_ON_COLOUR, (0, 0, 0))
        return self.npc_font.render(str('Angles Off'), False, Game.ANGLE_OFF_COLOUR, (0, 0, 0))

    def output_data(self):
        output = {"r": self.right_bat.rect.y,
                  "bx": self.ball.rect.x,
                  "by": self.ball.rect.y,
                  "score": self.score}
        return output

    def prepare_data(self, data_hash):
        array = list(data_hash.values())[:3]
        numpy_array = np.array(array)
        return numpy_array

    def update_epsilon(self):
        if self.epsilon > 0.1:
            self.epsilon -= 0.00001

    def get_reward(self):
        if self.score['p1'] - self.old_score['p1'] > 0:
            reward = -700
            self.old_score = dict(self.score)
        elif self.ball.rect.colliderect(self.right_bat):
            reward = 700
            self.old_score = dict(self.score)
        else:
            reward = 0
        return reward

    def game_score(self):
        return f"{self.score['p1']}   :   {self.score['p2']}"


    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:  # pylint: disable=undefined-variable
                    if event.key == K_ESCAPE:  # pylint: disable=undefined-variable
                        self.robotron3000.model.save('test.h5')
                        self.running = False
            if self.ball.reset:
                self.ball.reset_ball()
            self.screen.fill((0, 0, 0))
            self.clock.tick()
            self.robotron3000.receive_state(self.prepare_data(self.output_data()), self.epsilon)
            self.ball.rect.move_ip(self.ball.speed)
            self.ball.update(self.score)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.ball.surf, self.ball.rect)
            self.screen.blit(self.left_bat.surf, self.left_bat.rect)
            self.screen.blit(self.right_bat.surf, self.right_bat.rect)
            self.screen.blit(self.font.render(self.game_score(), 1, (255, 255, 255)),
                             (self.X_MIDDLE_SCREEN -40, 10))
            self.check_bat_move()
            self.check_if_ball_angles_on()
            self.turn_angles_on_or_off()
            self.turn_npc_on_or_off()
            self.turns_on_ball_3d()

            self.screen.blit(self.print_npc_status(), (30, 30))
            self.screen.blit(self.print_angle_status(), (665, 30))
            if self.npc_on:
                self.moves_npc_player()
            self.print_npc_status()
            print(self.prepare_data(self.output_data()))
            self.robotron3000.update_state(self.prepare_data(self.output_data()))
            self.update_epsilon()
            print(self.epsilon)
            print(self.output_data())
            pygame.display.flip()

if __name__ == "__main__":
    GAME = Game()
    GAME.game_loop()
