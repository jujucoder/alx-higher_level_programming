#!/usr/bin/python3
def no_c(my_string):
    string = ''
    j = 0
    for i in my_string:
        if i != 'C' and i != 'c':
            string += i
            j += 1
    return string
