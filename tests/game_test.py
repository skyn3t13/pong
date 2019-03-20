import pytest
from ping.game import Game

def test_screen_is_rendered():
    game = Game()
    assert game.screen.get_height() == 600
    assert game.screen.get_width() == 800


def test_ball_is_drawn():
    game = Game()
    assert repr(game.ball.rect) == '<rect(400, 300, 25, 25)>'


def test_ball_moves_from_starting_position():
    game = Game()
    game.game_loop()
    assert repr(game.ball.rect) != '<rect(400, 300, 25, 25)>'
