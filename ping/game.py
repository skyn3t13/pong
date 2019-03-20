import pygame
from pygame.locals import *
from ping.ball import Ball

class Game:

    HEIGHT = 600
    WIDTH = 800


    def __init__(self, ball = Ball()):

        pygame.init()
        self.screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.ball = ball
        self.ball.rect.y = self.HEIGHT / 2
        self.ball.rect.x = self.WIDTH / 2
        self.background = pygame.Surface(self.screen.get_size())
        # self.background.fill((135, 206, 250))

    def game_loop(self):

        self.running = True
        self.rect = self.screen.get_rect()

        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

            self.ball.rect.move_ip(self.ball.speed)
            self.ball.update()
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.ball.surf, self.ball.rect)
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.game_loop()
