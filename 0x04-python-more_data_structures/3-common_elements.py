#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Create an empty set to store the common elements
    common = set()

    # Iterate over the elements in the first set
    for element in set_1:
        # Check if the element is present in the second set
        if element in set_2:
            # Add the element to the common set
            common.add(element)

    return common
