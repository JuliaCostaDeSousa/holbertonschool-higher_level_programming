#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        list_values = list(a_dictionary.values())
        list_key = list(a_dictionary.keys())
        return (list_key[list_values.index(max(list_values))])
