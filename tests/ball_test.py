from ping.ball import Ball
import random

def test_update_blocks_top_of_screen():
    ball = Ball(300, 400)
    ball.rect.top = -1
    score = {"p1": 0, "p2": 0}
    ball.update(score)
    assert ball.rect.top == 0

def test_update_blocks_bottom_of_screen():
    ball = Ball(300, 400)
    ball.rect.bottom = 601
    score = {"p1": 0, "p2": 0}
    ball.update(score)
    assert ball.rect.bottom == 600

def test_reverse_vertical_direction():
    ball = Ball(300, 400)
    speed = ball.speed[1]
    ball.reverse_vertical_direction()
    assert ball.speed[1] == -speed

def test_stop_ball():
    ball = Ball(300, 400)
    ball.stop_ball()
    assert ball.speed == (0, 0)

def test_set_ball_speed():
    ball = Ball(300, 400)
    ball.set_ball_speed(100, 100)
    assert ball.speed == (100, 100)

def test_reset_ball():
    ball = Ball(300, 400)
    ball.rect.x = 0
    ball.rect.y = 0
    ball.set_ball_speed(100, 100)
    random.seed(0)
    ball.reset_ball()
    assert ball.rect.x == 300
    assert ball.rect.y == 400
    assert ball.speed == (10, 0)

def test_set_random_angle():
    ball = Ball(300, 400)
    speed = ball.speed[0]
    random.seed(0)
    ball.set_random_angle()
    assert ball.speed[0] == -speed
    assert ball.speed[1] == (10 - speed)

def test_angle_limiter():
    ball = Ball(300, 400)
    ball.speed = (10, 12)
    ball.angle_limiter(2)
    assert ball.speed[0] == 2
