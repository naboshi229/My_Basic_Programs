import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
quan_of_letters = 0
quan_of_symbols = 0
quan_of_numbers = 0
password_list = []
def check_user_input(x, y, z):
    while True:
        try:
            x = int(input(f"How many {y} would you like in your password?\n"))
            while True:
                if x <= 0:
                    x = int(input(f'Incorrect {y}, please enter a number that isn\'t equal to "0" or isn\'t negative!!!\nHow many {y} would you like in your password?\n'))
                else:
                    break
            break
        except ValueError:
            print("Please enter a number, not a word or letter!!!")
    for char in range(1, x + 1):
        password_list.append(random.choice(z))

print("Welcome to the Python Password Generator! :D")

check_user_input(quan_of_letters, "letters", letters)
check_user_input(quan_of_symbols, "symbols", symbols)
check_user_input(quan_of_numbers, "numbers", numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}\nEnjoy!!! :P")
