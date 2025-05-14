#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list or len(my_list) == 0:
        return None
    else:
        new_list = []
        for i in range(len(my_list)):
            if (my_list[i] == search):
                new_list.append(replace)
            else:
                new_list.append(my_list[i])
        return new_list
