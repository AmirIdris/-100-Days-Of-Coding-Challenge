from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

    def stretch(self):
        self.shapesize(stretch_wid=5, stretch_len=1)

    def give_position(self, prop):
        if prop == "first":
            self.stretch()
            self.goto(-320, 0)

        if prop == "second":
            self.stretch()
            self.goto(320, 0)

        if prop == "center":
            self.shapesize(stretch_wid=0.5, stretch_len=0.5)





