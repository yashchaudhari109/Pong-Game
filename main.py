from turtle import Screen, Turtle
from scoreboard import Scoreboard
from divider import Divider
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("pong_game (use key W & S for left paddle and I & J for right paddle)")
screen.tracer(0)

# two paddle created
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
divider = Divider()

screen.listen()
screen.onkey(r_paddle.go_up, "i")
screen.onkey(r_paddle.go_down, "j")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")




ball = Ball()
scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when ball misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score2()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score1()



screen.exitonclick()