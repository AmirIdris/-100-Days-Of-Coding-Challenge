# This is a sample Python script.
from paddle import Paddle
from turtle import Screen, Turtle
from ball import Ball
from score_board import ScoreBoard
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=800)
screen.title("Pong Game")
screen.tracer(0)

# creating The  Paddles and Positioning it on the screen
first_paddle = Paddle((340, 0))
second_paddle = Paddle((-340, 0))
screen.listen()
screen.onkey(first_paddle.move_the_paddle_up, "Up")
screen.onkey(first_paddle.move_the_paddle_down, "Down")
screen.onkey(second_paddle.move_the_paddle_up, "w")
screen.onkey(second_paddle.move_the_paddle_down, "s")

# creating the Ball
ball = Ball()
# creating Score Board
score_board = ScoreBoard()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision of the ball to the right paddle
    if ball.distance(first_paddle) < 50 and ball.xcor() > 320 or ball.distance(second_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when the first paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.left_point()
    # detect when the second paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.right_point()


screen.exitonclick()