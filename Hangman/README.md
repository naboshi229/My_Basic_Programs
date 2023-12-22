# Hangman
## Description
This is a game where user needs to guess letter by letter randomly generatedwords by program from Hangman_Words.py file.
## Flow Chart for this game
/[Hangman/Hangman-Flow-Chart.png](https://github.com/naboshi229/My_Basic_Programs/blob/main/Hangman/Hangman-Flow-Chart.png)/
## How my hangman game works line by line
- Firstly I imported module random, then logo and stage (from Hangman_Art.py file) and world_list from (Hangman_Words.py file).
- chosen_word stores randomly chose by program variable from list word_list (Hangman_Words.py file).
- (display) is set to blank (no character) string, word_length is a length of the previosuly chosen word from list,end_of_game is set to False and lives are assigned to integer number 6.
- Then program prints logo from the previosuly imported variable logo (from Hangman_Art.py file).
- In for loop that is in range of the word_length variable, I've added "_" blank spots to the display list in order to show user the encrypted word to guess with proper length.
- After that there is a while loop which works while end_of_game is assigned to false (I used "not" and value "False" to make my program more clear).
- In a while loop user firstly is asked for input which is assigned to guess and lowered (in case if user will use capital or lowercase letter).
- For loop goes through chosen_word list. If statement in for loop checks if guessed letter by user (guess) equals to the letter stored in chosen_word list.
If this condition is true that letter is assigned to that position in chosen_word list.
- Later another if statement checks if user's guess (guess) is not stored in chosen_word list. If that statement is true program prints to the user in f string:
"You've guessed {guess}, that's not in the word. You lose a life!!!" then program subtracts one from lives. Second if statements checks the status of lives,
if they are equal to 0, end_of_game is assigned to true and program prints "You lose!!! :(", while loop breaks.
- If user hasn't run out of lives program shows current stage of guessed words. Displaying letters that user guessed and "_" for letters that user still hasn't guessed in a display variable.
- Last if statements checks if display has any "_" value if there is none of them, end_of_game assignes to True and program prints to user "You win!!! :)", while loop breaks here too.
- print at the end shows user using ASCII images (from Hangman_Art.py file) ![Hangman Flow Chart]
that are stored in stages list which shows appropiate picture to the value of lives.
### That's it for that game, I wanted to describe it throughly just in case I will come back to it someday! :D
