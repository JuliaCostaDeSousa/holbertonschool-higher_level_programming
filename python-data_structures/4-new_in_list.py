#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > len(my_list) or my_list[idx] < 0:
        return my_list
    else:
        list_copy = my_list.copy()
        list_copy[idx] = element
        return list_copy
