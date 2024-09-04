import string
import time
import random

POSSIBLE_CHARACTERS = string.printable
DELAY_PER_INPUT = 0.005

def scrolling(desired):
    index = 0
    current_string = ""
    while current_string != desired:
        while current_string != desired[:index+1]:
            time.sleep(DELAY_PER_INPUT)
            char = POSSIBLE_CHARACTERS[random.randrange(0, len(POSSIBLE_CHARACTERS)-1)]
            print(current_string + str(char))
            if str(char) == desired[index]:
                index += 1
                current_string += char
                break

scrolling("This is a scrolling printer!")