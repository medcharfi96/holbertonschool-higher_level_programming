#!/usr/bin/python3
import sys
if __name__ == "__main__":
    somme = 0
    for i in range(1, len(sys.argv)):
        somme = somme + int(sys.argv[i])
    print("{}".format(somme))
