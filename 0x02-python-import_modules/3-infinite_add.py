#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    total = 0
    for item in argv:
        if item != argv[0]:
            total += int(item)
    print(total)
