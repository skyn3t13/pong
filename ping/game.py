import pygame
from pygame.locals import *
from ping.bat import Bat
from ping.ball import Ball

class Game:

    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 800
    COLOUR = (255, 255, 255)
    BAT_WIDTH = 10
    BAT_HEIGHT = 100

    def __init__(self, ball = Ball()):

        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Game.SCREEN_WIDTH,
                                               Game.SCREEN_HEIGHT))
        self.bats = Bat(Game.SCREEN_WIDTH,
                        Game.SCREEN_HEIGHT,
                        Game.BAT_WIDTH,
                        Game.BAT_HEIGHT)
        self.ball = ball
        self.ball.rect.y = self.HEIGHT / 2
        self.ball.rect.x = self.WIDTH / 2
        self.background = pygame.Surface(self.screen.get_size())

    def game_loop(self):
        self.rect = self.screen.get_rect()

        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, self.COLOUR, self.bats.left_bat)
            pygame.draw.rect(self.screen, self.COLOUR, self.bats.right_bat)
            self.clock.tick(60)
            self.ball.rect.move_ip(self.ball.speed)
            self.ball.update()
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.ball.surf, self.ball.rect)
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.game_loop()
