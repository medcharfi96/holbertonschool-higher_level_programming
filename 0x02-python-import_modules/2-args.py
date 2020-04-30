#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments.\n".format(len(sys.argv)-1), end='')
    elif len(sys.argv) == 2:
        print("{} argument:\n".format(len(sys.argv)-1), end='')
    else:
        print("{} arguments:\n".format(len(sys.argv)-1), end='')

    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))
