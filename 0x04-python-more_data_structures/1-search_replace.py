#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    result = []

    # Iterate over the elements in the input list
    for item in my_list:
        """If the current element matches the
        search element, replace it with the new element"""
        if item == search:
            result.append(replace)
        else:
            result.append(item)

    return result
