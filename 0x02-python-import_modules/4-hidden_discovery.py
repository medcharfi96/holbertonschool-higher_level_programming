#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for i in range(0, len(dir(hidden_4))):
        if i[0] != '_' and i[1] != '_':
            print("{:d}\n".format(i))
