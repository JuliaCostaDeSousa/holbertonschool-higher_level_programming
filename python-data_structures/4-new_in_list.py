#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list or idx >= len(my_list) or idx < 0:
        return my_list
    else:
        list_copy = my_list.copy()
        list_copy[idx] = element
        return list_copy
