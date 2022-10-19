from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}

try:
    data = pandas.read_csv("Data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("Data/arabic_words - Sheet1.csv")
    data_dict= data.to_dict(orient="records")

else:
    data_dict = data.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card, flip_timer, data_dict
    window.after_cancel(flip_timer)
    current_card = choice(data_dict)
    word = current_card["Amharic"]
    canvas.itemconfig(card_title, text="Amharic", fill="black")
    canvas.itemconfig(card_words, text=word, fill="black")
    canvas.itemconfig(canvas_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_the_card)


def flip_the_card():
    global current_card
    canvas.itemconfig(card_title, text="Arabic", fill="white")
    canvas.itemconfig(canvas_background, image=card_back_img)
    canvas.itemconfig(card_words, text=current_card["Arabic"], fill="white")


def known_word():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("Data/words_to_learn.csv")
    next_card()


# ------------------------------------------------UI Design ----------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# flipping the card after 3 seconds
flip_timer = window.after(3000, func=flip_the_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas_background = canvas.create_image(400, 263, image=card_front_image)
# canvas.create_text(text="Title")
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_words=canvas.create_text(400, 263, text="Arabic Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cancel_image = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=cancel_image, command=next_card, highlightthickness=0)
cancel_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, command=known_word, highlightthickness=0)
right_btn.grid(row=1, column=1)
next_card()

window.mainloop()
