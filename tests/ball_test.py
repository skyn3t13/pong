import pytest
from ping.ball import Ball


def test_update_blocks_top_of_screen():
    ball = Ball()
    ball.rect.top = -1
    ball.update()
    assert ball.rect.top == 0


def test_update_blocks_bottom_of_screen():
    ball = Ball()
    ball.rect.bottom = 601
    ball.update()
    assert ball.rect.bottom == 600

def test_reverse_vertical_direction():
    ball = Ball()
    speed = ball.y_speed
    ball.reverse_vertical_direction()
    assert ball.y_speed == -speed
