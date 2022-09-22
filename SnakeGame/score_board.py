from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Arial", 8, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT, move=False)

    def game_is_over(self):
        self.goto(0,0)
        self.write("Game Is Over ", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_score()








