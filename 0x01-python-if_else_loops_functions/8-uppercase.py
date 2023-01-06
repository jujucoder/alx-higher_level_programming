#!/usr/bin/python3

def uppercase(str):
    j = len(str) - 1
    for i in str:
        if i != str[j]:
            if i == ' ':
               print("{}".format(i), end='')
            else:
               print("{:c}".format(ord(i) - 32), end='')

        else:
             print("{:c}".format(ord(i) - 32))
