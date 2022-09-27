from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position[0], position[1])
        self.stretch()

    def stretch(self):
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_the_paddle_up(self):
        y_cord = self.ycor() + 50
        self.goto(self.xcor(), y_cord)

    def move_the_paddle_down(self):
        y_cord = self.ycor() - 50
        self.goto(self.xcor(), y_cord)





