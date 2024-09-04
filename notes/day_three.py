from formatting import intro, line_break, line_with_note

intro(3)

# Mod
# how would i determine if a number is odd or even?
# Use Modulus to find if their is a remainder when dividing by two
# if there is a remainder (1), the value of num is odd
# if there is no remainder (0), the value of num is even

# Example usage of mod
num = 5
print(num % 2) # Output: 1 (Odd)

num = 6
print(num % 2) # Output: 0 (Even)

line_break()

# Functions
# Functions are reusable blocks of code that perform a specific task.
# A function is defined using the 'def' keyword followed by the function name and parentheses.
# Inside the parentheses, you can specify any parameters that the function needs.

# Example: Cube function
# The cube function takes a number as input and returns its cube.
def cube(x):
    """
    Parameters:
    x (int or float): The number to be cubed.
    
    Returns:
    int or float: The cube of the input number.
    """
    return x**3

# Example usage of the cube function
print(cube(3))  # Output: 27

line_break()

# Functions Made in Class
def cube(x):
    return x**3

def total(subtotal, taxrate=0.05):
    return subtotal * taxrate + subtotal

print(total(114))