from turtle import Screen
from food import Food
from Snake import Snake
from score_board import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.listen()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision
    if snake.head.distance(food) < 15:
        score_board.increment_score()
        food.refresh()
        snake.add_segment()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # detect collision with body of the snake
    # if head collide with any segments in the tail
    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


screen.exitonclick()
