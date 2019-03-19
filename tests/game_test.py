import pytest
from ping.game import Game
from ping.ball import Ball

def test_screen_is_rendered():
    game = Game()
    assert game.screen.get_height() == 600
    assert game.screen.get_width() == 800


def test_escape_key_exits_game():
    game = Game()
    game.game_loop()
    assert repr(game.ball.rect) == '<rect(400, 300, 25, 25)>'
    assert game.rect.contains(game.ball.rect)

