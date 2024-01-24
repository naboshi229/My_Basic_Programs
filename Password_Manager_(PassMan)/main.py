from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# CONSTANTS
EMAIL = 'abcdef@gmail.com'
WHITE = '#E4DEBE'
LIGHT_BLUE = '#F0EDCF'
BLUE = '#0B60B0'
FONT_1 = ('Arial', 12, 'bold')
FONT_2 = ('Arial', 12)


# PASSWORD GENERATOR

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# SAVE PASSWORD

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title='Oops', message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details entered: \nEmail/Username: {email}\n'
                                               f'Password: {password}\nIs it ok to save?')

        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# UI SETUP
window = Tk()
window.title('Password Manager')
window.config(padx=35, pady=35, bg=WHITE)

# Image
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Label and Entry
website_label = Label(text='Website:', bg=WHITE, fg=BLUE, font=FONT_1)
website_label.grid(column=0, row=1)

website_entry = Entry(width=35, bg=LIGHT_BLUE, fg=BLUE, font=FONT_2)
website_entry.grid(column=1, row=1, padx=10, pady=10, columnspan=2, sticky='EW')
website_entry.focus()

# Email Label and Entry
email_label = Label(text='Email/Username:', bg=WHITE, fg=BLUE, font=FONT_1)
email_label.grid(column=0, row=2)

email_entry = Entry(width=35, bg=LIGHT_BLUE, fg=BLUE, font=FONT_2)
email_entry.grid(column=1, row=2, padx=10, pady=10, columnspan=2, sticky='EW')
email_entry.insert(0, EMAIL)

# Password Label and Entry
password_label = Label(text='Password:', bg=WHITE, fg=BLUE, font=FONT_1)
password_label.grid(column=0, row=3)

password_entry = Entry(width=21, bg=LIGHT_BLUE, fg=BLUE, font=FONT_2)
password_entry.grid(column=1, row=3, padx=10, pady=10, sticky='EW')

# Buttons
generate_password_button = Button(text='Generate Password', command=generate_password, bg=WHITE, fg=BLUE, font=FONT_1)
generate_password_button.grid(column=2, row=3, padx=10, pady=10)

add_button = Button(text='Add', command=save, padx=2, pady=2, width=36, bg=WHITE, fg=BLUE, font=FONT_1)
add_button.grid(column=1, row=4, padx=10, pady=10, columnspan=2, sticky='EW')

window.mainloop()
