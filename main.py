bill = float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
percentage /= 100
tip = bill * (1 + percentage)
result = tip / people
print(f'Each person should pay: ${round(result, 2)}')