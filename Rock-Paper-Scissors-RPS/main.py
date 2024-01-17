import random
import ascii_rps

game_images = [ascii_rps.rock, ascii_rps.paper, ascii_rps.scissors]

while True:
    try:
        user_choice = int(input('What do you choose? Type "0" for Rock, "1" for Paper or "2" for Scissors.\n'))
        while True:
            if user_choice == 0 or user_choice == 1 or user_choice == 2:
                break
            else:
                user_choice = int(input('A number is to high/low! Try only using [0,1,2]! :(\nType "0" for Rock, "1" for Paper or "2" for Scissors!\n'))
        break
    except ValueError:
        print("Please enter a number, not a word or letter!")
computer_choice = random.randint(0,2)
print(game_images[user_choice])
print(f"Computer chose:"+game_images[computer_choice])

if user_choice == 0 and computer_choice == 2 or user_choice == 2 and computer_choice == 1 or user_choice == 1 and computer_choice == 0:
    print("You win!!! Lessgo!!! :P")
elif user_choice == 2 and computer_choice == 0 or user_choice == 1 and computer_choice == 2 or user_choice == 0 and computer_choice == 1:
    print("You lose! :/\nGG and GL next time! :D")
elif user_choice == computer_choice:
    print("It's a draw!\nGL next time! :D")
