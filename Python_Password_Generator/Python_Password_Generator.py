import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator! :D")

while True:
    try:
        quan_of_letters = int(input("How many letters would you like in your password?\n"))
        while True:
            if quan_of_letters <= 0:
                quan_of_letters = int(input('Incorrect number, please enter a number that isn\'t equal to "0" or isn\'t negative!!!\nHow many letters would you like in your password?\n'))
            else:
                break
        break
    except ValueError:
        print("Please enter a number, not a word or letter!!!")
while True:
    try:
        quan_of_symbols = int(input("How many symbols would you like to have in your password?\n"))
        while True:
            if quan_of_symbols <= 0:
                quan_of_symbols = int(input('Incorrect number, please enter a number that isn\'t equal to "0" or isn\'t negative!!!\nHow many symbols would you like in your password?\n'))
            else:
                break
        break
    except ValueError:
        print("Please enter a number, not a word or letter!!!")
while True:
    try:
        quan_of_numbers = int(input("How many numbers would you like to have in your password?\n"))
        while True:
            if quan_of_numbers <= 0:
                quan_of_numbers = int(input('Incorrect number, please enter a number that isn\'t equal to "0" or isn\'t negative!!!\nHow many numbers would you like in your password?\n'))
            else:
                break
        break
    except ValueError:
        print("Please enter a number, not a word or letter!!!")

password_list = []

for char in range(1, quan_of_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, quan_of_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, quan_of_numbers + 1):
    password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}\nEnjoy!!! :P")













