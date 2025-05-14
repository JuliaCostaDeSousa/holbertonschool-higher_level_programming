#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None
    else:
        myset = set(my_list)
        return sum(myset)
