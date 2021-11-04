"""CLI application for a prefix-notation calculator."""
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



# Repeat forever
while True:

    # Get equation from user
    equation = input("Your equation: ")

    # Tokenize equation
    token = equation.split(" ")

    # Input validation
    #Too few entries
    if token[0] in ["+", "-", "*", "power", "/", "mod"] and len(token) < 3:
        print("Enter two numbers.")
        continue

    # Non-numeric Entries
    if not token[1].isdigit() or not token[2].isdigit():
        print ("please enter a number")
        continue

    # Invalid arithmetic symbol
    if token[0] not in ["+", "-", "*", "power", "square", "/", "cube", "mod"]:
        print ("Invalid Arithmatic")  
    
    # assign variables to tokens and float
    arith = token[0]

    # assign variable if token[1]/token[2] exist
    if len(token) == 2:
        num1 = float(token[1])
        
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