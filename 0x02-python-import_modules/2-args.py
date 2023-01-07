#!/usr/bin/python3
from sys import argv

argc = len(argv) -1
if argc == 1:
    print("{} argument".format(argc))
    print("{} : {}".format(argc, argv[argc]))

else:
    print("{} arguments".format(argc))
    if argc != 0:
        for i in range(1, argc + 1):
            print("{} : {}".format(i, argv[i]))

