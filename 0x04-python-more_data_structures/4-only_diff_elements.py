#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Find the elements that are present in only one set
    diff_elements = (set_1 - set_2) | (set_2 - set_1)

    return diff_elements

