# Python_Password_Generator
## Description
This is program generates random string of characters using user's input as an quantity.
## Quick note
Python_Password_Generator.py is the only file you need in order for my program to work.
## How my program works line by line
- I imported random module for this which allowed me to use random.choice and random.shuffle methods.
- I executed list of letters, numbers and symbols containg all of characters used for making random passwords by my program. I exectued quan_of_letters, quan_of_symbols and quan_of_numbers that will hold integer number variable as an user's input for quantity of letters, numbers and symbols. Lastly I executed password_list as a list that will store all of randomly generated characters for my result which is password.
- Then program greats user with a message "Welcome to the Python Password Generator! :D".
- Later asks user for the quntity of letters, symbols and numbers exectued by the def function called check_user_input(). Which by default is storing appropriately as a variable x. Variable y holds string variable used in f string (that asks user for appropriate input in a question)  and z is later took appropriately as a (letters, symbols, numbers) lists.
- Every user's input is checked by two while loops and (try and expect) statement, which expects the type of error (ValueError) if user tries to pass anything besides integer number. Second while loop checks if the number is greater than and not equal to 0.
- After breaking those two while loops (ofc if every statement is True) that checks user's input, for loop generates (using random.choice method from random module), using y (so letters, symbols or numbers) with the quantity x depended on user's input (quan_of letters, quan_of_symbols, quan_of_numbers).
- After executing def funtction check_user_input() I used a random.shuffle method from random module. (which allowed me to shuffle every's character placement in my password_list list)
- Then I added every's password_list character to vairriable password (which I assigned to string type, ofc before executing for loop) using for loop.
## What I managed to improve later
- I added function in order to not repeat the same line of code six times.
### That will be it for now!
