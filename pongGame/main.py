# This is a sample Python script.
from paddle import Paddle
from turtle import Screen
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=800)
screen.title("Pong Game")

# creating The First Paddle
first_paddle = Paddle()
first_paddle.give_position(prop="first")

#creating The Second Paddle.
second_paddle = Paddle()
second_paddle.give_position(prop="second")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


screen.exitonclick()