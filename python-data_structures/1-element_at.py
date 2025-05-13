#!/usr/bin/python3
def element_at(my_list, idx):
    if not my_list or idx >= len(my_list) or idx < 0:
        return None
    else:
        return my_list[idx]
