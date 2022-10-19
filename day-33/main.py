# requesting an api using python request modules
import requests
from tkinter import *
# data = requests.get("https://api.kanye.rest").json()
# print(data["quote"])


def get_quote():
    quote = requests.get("https://api.kanye.rest").json()
    canvas.itemconfig(quote_label, text=quote["quote"])


# ----------------------------------------------UI DESIGN -------------------------------------------------
window = Tk()
window.title("Kanye Once Says")
window.config(padx=25, pady=25)

canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="Data/img.png")
canvas.create_image(150, 270, image=background_image)
quote_label = canvas.create_text(150, 270, text="Kanye quote goes hear", font=("Arial", 8, "italic"))
canvas.grid(row=0, column=0)
kanye_image = PhotoImage(file="Data/img_1.png")
kanye_button = Button(image=kanye_image, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
get_quote()
window.mainloop()


