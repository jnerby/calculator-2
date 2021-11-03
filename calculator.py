"""CLI application for a prefix-notation calculator."""
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



# Repeat forever
while True:

    # Get equation from user
    equation = input("Your equation: ")

    # Tokenize equation
    token = equation.split(" ")

    # assign variables to tokens and float
    arith = token[0]
    num1 = float(token[1])
    
    # assign variable if token[2] exists
    if len(token) == 3:
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
        # divide
        elif arith == "/":
            print(divide(num1, num2))
        # square
        elif arith == "square":
            print(square(num1))
        # cube
        elif arith == "cube":
            print(cube(num1))
        # power
        elif arith == "pow":
            print(power(num1, num2))
        # mod 
        elif arith == "mod":
            print(mod(num1, num2))