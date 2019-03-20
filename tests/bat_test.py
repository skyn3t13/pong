import pytest
from ping.bat import Bat


def test_bat_drawn_correctly():
    bat = Bat(1600, 10, 100, 0, 800)
    assert repr(bat.rect) == '<rect(0, 800, 10, 100)>'


def test_bat_move_up():
    bat = Bat(1600, 10, 100, 0, 800)
    bat.move_up(10)
    assert repr(bat.rect) == '<rect(0, 790, 10, 100)>'


def test_bat_move_down():
    bat = Bat(1600, 10, 100, 400, 400)
    bat.move_down(10)
    assert repr(bat.rect) == '<rect(400, 410, 10, 100)>'
