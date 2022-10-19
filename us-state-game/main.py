from turtle import Turtle, Screen


screen = Screen()
turtle = Turtle()
screen.title("U.S. State Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput("Guess The State", prompt="What is another States Name")
print(answer_state)


screen.exitonclick()