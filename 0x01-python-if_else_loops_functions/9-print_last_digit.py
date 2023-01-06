#!/usr/bin/python3
def print_last_digit(number):
    if type(number) == str:
        raise
    number = str(number)
    print(number[-1], end='')
    return number[-1]
