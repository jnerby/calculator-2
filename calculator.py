"""CLI application for a prefix-notation calculator."""
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



# Repeat forever
while True:

    # Get equation from user
    equation = input("Your equation: ")

    # Tokenize equation
    token = equation.split(" ")

    arith = token[0]
    num1 = float(token[1])
    num2 = float(token[2])

    # Quit if first token is q
    if token[0] == "q":
        quit()
    else:
        #Add function
        if arith == "+":
            print(add(num1, num2))
        # Subtract
        elif arith == "-":
            print(subtract(num1, num2))
        # multiply
        elif arith == "*":
            print(multiply(num1, num2))