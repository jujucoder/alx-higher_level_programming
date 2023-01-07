#!/usr/bin/python3
if __name__ == '__main__':
    def print_list_integer(my_list=[]):
        if len(my_list) != 0:
            for i in range(0, len(my_list)):
                print("{:d}".format(my_list[i]))
            
