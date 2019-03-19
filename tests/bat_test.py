import pytest
from ping.bat import Bat

def test_left_bat_drawn_correctly():
    bats = Bat(1600, 800, 10, 100)
    assert bats.left_bat == ''

def test_right_bat_drawn_correctly():
    bats = Bat(1600, 800, 10, 100)
    assert bats.right_bat == ''