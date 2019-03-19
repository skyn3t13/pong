import pytest
from ping.bat import Bat

def test_left_bat_drawn_correctly():
    bats = Bat(1600, 800, 10, 100)
    assert repr(bats.left_bat) == '<rect(0, 350, 10, 100)>'

def test_right_bat_drawn_correctly():
    bats = Bat(1600, 800, 10, 100)
    assert repr(bats.right_bat) == '<rect(1590, 350, 10, 100)>'
