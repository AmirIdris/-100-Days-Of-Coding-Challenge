import tkinter
# creating new GUI Windows
window = tkinter.Tk()
window.title("My First GUI Window")
window.minsize(500, 300)

# create new label on the window using below codes
new_label = tkinter.Label(text="My New label is Here:", font=("Arial", 15, "bold"))
new_label.pack()

# changing the value of the label using config method and dictionary
new_label["text"] = "My New Text"
# new_label.config(text="Text From Config")


# Perform Some action after the button is clicked
def button_clicked():
    input_text = provide_input.get()
    new_label.config(text=input_text)


# creating Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Providing Data Using Input
provide_input = tkinter.Entry()
provide_input.pack()
print(provide_input.get())


# keep the windows visible using the code below
window.mainloop()

