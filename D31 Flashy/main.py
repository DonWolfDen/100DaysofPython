from tkinter import Tk, PhotoImage, Canvas, Button
import pandas as pa
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pa.read_csv("data/german_to_learn.csv")
except FileNotFoundError:
    data = pa.read_csv("data/german_words.csv")
    data.to_csv("data/german_to_learn.csv", index=False)

to_learn = data.to_dict(orient="records")
current_card = {}


def flip_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=current_card["English"])

def next_card():
    global current_card
    current_card = choice(to_learn)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(title, text="German")
    canvas.itemconfig(word, text=current_card["German"])
    global timer
    window.after_cancel(timer)
    timer = window.after(3000, flip_card)

def remove_card():
    to_learn.remove(current_card)
    pa.DataFrame(to_learn).to_csv("data/german_to_learn.csv", index=False)

    try:
        data = pa.read_csv("data/german_learned.csv")
    except:
        with open("data/german_learned.csv", "w") as data_file:
            data_file.write("German,English")
        data = pa.read_csv("data/german_learned.csv")

    data = data.to_dict(orient="records")
    data.append(current_card)
    pa.DataFrame(data).to_csv("data/german_learned.csv", index=False)

    next_card()



window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right = PhotoImage(file="images/right.png")
correct = Button(image=right, highlightthickness=0, command=remove_card)
correct.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png")
incorrect = Button(image=wrong, highlightthickness=0, command=next_card)
incorrect.grid(column=0, row=1)

next_card()




window.mainloop()




