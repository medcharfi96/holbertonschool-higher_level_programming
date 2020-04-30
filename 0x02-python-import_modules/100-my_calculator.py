#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    zeb = sys.argv
    if len(sys.argv) == 4:
        opr = zeb[2]
        a = int(zeb[1])
        z = int(zeb[3])
        if (opr != "+" and opr != "*" and opr != "-" and opr != "/"):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        elif zeb[2] == "*":
            print("{:d} + {:d} = {:d}".format(a, z, mul(a, z)))
        elif zeb[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, z, add(a, z)))
        elif zeb[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, z, sub(a, z)))
        elif zeb[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, z, div(a, z)))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
