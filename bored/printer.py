import string
import time
import random

POSSIBLE_CHARACTERS = string.printable

def scrolling(desired, delay=0.005):
    index = 0
    current_string = ""
    while current_string != desired:
        while current_string != desired[:index+1]:
            time.sleep(delay)
            char = POSSIBLE_CHARACTERS[random.randrange(0, len(POSSIBLE_CHARACTERS)-1)]
            print(current_string + str(char))
            if str(char) == desired[index]:
                index += 1
                current_string += char
                break

scrolling("This is a scrolling printer!")