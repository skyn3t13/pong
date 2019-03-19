import pygame
from pygame.locals import *

class Game:

    HEIGHT = 600
    WIDTH = 800


    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))



    def game_loop(self):

        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False



if __name__ == "__main__":
    game = Game()
    game.game_loop()
