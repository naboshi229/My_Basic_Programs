from tkinter import *
import pandas
import random

BG_COLOR = "#B1DDC6"
FONT_TITLE = ('Ariel', 40, 'italic')
FONT_WORD = ('Ariel', 60, 'bold')

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/polish_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='Polish', fill='black')
    canvas.itemconfig(card_word, text=current_card['Polish'], fill='black')
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_bg, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BG_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text='', font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
