"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    sum = num1 + num2
    return sum


# def add_list(lst):
#     """Return the sum of the two inputs."""
#     sum = 0
#     for num in lst:
#         sum += num
#     return sum


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    diff = num1 - num2
    return diff


def multiply(num1, num2):
    """Multiply the two inputs together."""
    # prod = num1 * num2
    return num1 * num2

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    return num1 / num2

def square(num1):
    """Return the square of the input."""
    return num1 * num1

def cube(num1):
    """Return the cube of the input."""
    return num1 * num1 *num1

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return num1**num2

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return num1 % num2

def add_mult(num1, num2, num3):
    """Get the sum of num1 and num2, then multiply sum with num3."""
    return (num1 + num2) * num3

def add_cubes(num1, num2):
    """Add the cubes of num1 and num2."""
    return cube(num1) + cube(num2)