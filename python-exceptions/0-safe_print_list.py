#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            break
    print()
    return count
