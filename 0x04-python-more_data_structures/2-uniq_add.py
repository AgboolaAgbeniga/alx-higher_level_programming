#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()

    # Iterate over the elements in the input list
    for num in my_list:
        # Add the unique integers to the set
        unique_integers.add(num)

    # Calculate the sum of unique integers
    total = sum(unique_integers)

    return total
