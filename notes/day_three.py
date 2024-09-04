from formatting import intro, line_break, line_with_note

intro(2)

print("how would i determine if a number is odd or even?")

num = 1234568798564
print("Odd") if num % 2 != 0 else print("Even")


def cube(x):
    return x**3

def total(subtotal, taxrate=0.05):
    return subtotal * taxrate + subtotal

print(total(114))