import pygame
from ping.player import Player


def test_player_is_created():
    player = Player(pygame.K_w, pygame.K_s)
    assert repr(player.key_up) == '119'
    assert repr(player.key_down) == '115'
