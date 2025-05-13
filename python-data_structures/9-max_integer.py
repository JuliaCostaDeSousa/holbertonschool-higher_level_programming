#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None
    else:
        my_list.sort(reverse=True)
    return my_list[0]
