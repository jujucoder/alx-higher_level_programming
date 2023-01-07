#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for i in sorted(range(len(my_list)), reverse = True):
            print("{:d}".format(my_list[i]))
