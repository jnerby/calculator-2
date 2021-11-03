"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# get equation from user
equation = input("Your equation: ")

#Tokenize equation
token = equation.split(" ")

