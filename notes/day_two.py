from formatting import intro, line_break, line_with_note

intro(2)

# Print the datatype of a value
print(type(1))
print(type("i am a string"))
print(type(3.14))

line_break()

# variables can change type at runtime
x = 5.2
print("Value of x:", x)
print("Type of the variable x:", type(x))

line_break()

# the x variable can be reassigned to a different value hence changing the variable type
x = 2
print("New value of x:", x)
print("New type of the variable x:", type(x))

line_break()

# y = x is not linked, y is only assigned the value of x
y = x
print("Value of x:", x)
print("Value of y:", y)

# changing the value of x does not affect y
x = 4
print("New value of x:", x)
print("New value of y:", y)

line_break()

# this can concat
print("hello " + "world")

# this will give an error because an integer can NOT be added to a string
print("Hello world!" + 1)

# a simple solution is converting the integer to a string str(1)
print("Hello world!" + str(1))

line_with_note("NEW MATH OPERATORS")

# this operator divides
print(20 / 7)

# this operator divides to floor value
print(20 // 7)

# this operator gets the remainder
print(20 % 7)

# IMPORTANT NOTE!!
# math follows PEMDAS unless otherwise specified with
# precidence indicated by perenthesis

line_break()

