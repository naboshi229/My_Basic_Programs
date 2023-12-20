when_the = "When the number is divisible by "
program_prints = " then program prints "
rules = ('Welcome to the FizzBuzz game!!!\nRules are simple:\n*' + when_the + '"3"' + program_prints + '"Fizz";\n*' + when_the + '"5"' + program_prints + '"Buzz";\n*' + when_the + '"3 and 5"' + program_prints + '"FizzBuzz".')
print(rules)
while True:
    try:
        target = int(input('Please type a number that is higher than "0" and "is whole (without any fractions) and positive":\n'))
        while True:
            if target > 0:
                break
            else:
                target = int(input('Incorrect value!!! (Your number is lower than 0 or is equal to 0)\nPlease type a number that is higher than "0" and "is whole (without any fractions) and positive":\n'))
        break
    except ValueError:
        print("Please enter a whole number (without any fractions) also your input mustn't be a word or letter!!!")
for number in range(1, target + 1):
    if number%3 == 0 and number%5 == 0:
        print(f"FizzBuzz ({number})")
    elif number%3 == 0:
        print(f"Fizz ({number})")
    elif number%5 == 0:
        print(f"Buzz ({number})")
    else:
        print(number)
print("\nThat's everything :)")