from calculator_art import logo
def add(n1, n2):
    """Adds one number to another"""
    return n1 + n2
def subtract(n1, n2):
    """Subtracts one number from another"""
    return n1 - n2
def multiply(n1, n2):
    """Multiplies one number by another"""
    return n1 * n2
def divide(n1, n2):
    """Divides one number by another"""
    return n1 / n2
def power(n1, n2):
    """Powers one number by another"""
    return pow(n1, n2)
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f'Type "y" to continue calculating with {answer} or type "n" to start a new calculation: ') == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
