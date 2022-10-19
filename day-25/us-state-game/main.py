from turtle import Turtle, Screen
import pandas as pd


guessed_state = []


def return_data_from_csv(state_name):
    data = pd.read_csv("50_states.csv")
    state_lookup = data[data["state"] == state_name]
    guessed_state.append(state_lookup)
    return state_lookup


def write_name_of_the_state_to_locations(data_frame):
    write_to_turtle = Turtle()
    write_to_turtle.hideturtle()
    write_to_turtle.penup()
    write_to_turtle.goto(int(data_frame["x"]), int(data_frame["y"]))
    write_to_turtle.write(data_frame.state.item())


screen = Screen()
turtle = Turtle()
screen.title("U.S. State Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while len(guessed_state) < 50:
    answer_state = screen.textinput("Guess The State", prompt="What is another States Name")
    state_frame = return_data_from_csv(state_name=answer_state)
    write_name_of_the_state_to_locations(data_frame=state_frame)


screen.exitonclick()