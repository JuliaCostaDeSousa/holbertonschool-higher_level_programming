#!/usr/bin/python3
import sys
add = 0
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(0)
    elif len(sys.argv) == 2:
        print(sys.argv[1])
    else:
        for i in range(1, len(sys.argv)):
            add += int(sys.argv[i])
        print(add)
