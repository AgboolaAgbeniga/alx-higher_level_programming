#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    result = []

    # Iterate over the elements in the input list
    for item in my_list:
<<<<<<< HEAD
        """If the current element matches the
        search element, replace it with the new element"""
=======
        """If the current element matches
        the search element, replace it with the new element"""
>>>>>>> 51b898b8892ea35c6981c33ec57f6765e37b9cd8
        if item == search:
            result.append(replace)
        else:
            result.append(item)

    return result
