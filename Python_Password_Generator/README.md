# Python_Password_Generator
This is program that generates random string of characters using user's input.
I imported random module for this which allowed me to use random.choice and random.shuffle methods.
Program greats user with a message "Welcome to the Python Password Generator! :D".
Then asks user for the number of letters, symbols and numbers.
Every user's input is checked by two while loops and (try and expect) statement, which expects the type of error (ValueError) if user tries to pass anything besides integer number. Second while loop checks if the number is greater than and not equal to 0.
After repeating similar line of code three times (I know I could use def for that, but I still don't know how to use it properly), maybe I can update this code in the future with that method. 
I executed password_list as a list that will store all of the character for my result which is password.
There are three for loops (which like I said before, I know that I could use a def method for that too). Those three for loops generates as follows (using random.choice method from random module) random letters, symbols and numbers with the quantity depended on user's input.
After executing those lines of code I used a random.shuffle method from random module. (which allowed me to shuffle every's character placement in my password_list list)
Then I added every's password_list character to vairriable password (which I assigned to string type, ofc before executing for loop) using for loop.
At the end program prints in f string f"Your password is: {password}\nEnjoy!!! :P"
