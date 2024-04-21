from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

#                                                  Setting Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(0)

#                                                  Setting Paddle


r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detecting collision with PADDLES
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9

    # Detecting when r_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball.move_speed *= 0.6

    # Detecting when l_paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball.move_speed *= 0.6

screen.exitonclick()
