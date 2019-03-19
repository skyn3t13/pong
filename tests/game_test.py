import pytest
from ping.game import Game

def test_screen_is_rendered():
    game = Game()
    assert game.screen.get_height() == 600
    assert game.screen.get_width() == 800


def test_escape_key_exits_game():
    game = Game()
