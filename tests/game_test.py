import numpy as np
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
    game.ball.rect.move_ip((10, 10))
    assert repr(game.ball.rect) != '<rect(400, 300, 25, 25)>'
    assert repr(game.ball.rect) == '<rect(410, 310, 25, 25)>'


def test_output_data():
    game = Game()
    assert game.output_data() == {'l': 300,
                                  'r': 300,
                                  'bx': 400,
                                  'by': 300,
                                  'score': {'p1': 0, 'p2': 0}}


def test_prepare_data():
    game = Game()
    numpy_array = game.prepare_data(game.output_data())
    assert np.array_equal(numpy_array, [300, 300, 400, 300])


def test_game_score():
    game = Game()
    game.score = {"p1": 0, "p2": 1}
    assert game.game_score() == f"0   :   1"
