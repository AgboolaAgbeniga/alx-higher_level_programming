#!/usr/bin/python3

def best_score(a_dictionary):
    # Initialize variables to track the best score and key
    best_key = None
    best_score = float('-inf')  # Initialize with negative infinity

    # Iterate over the key-value pairs in the dictionary
    for key, value in a_dictionary.items():
        # Check if the current value is greater than the best score
        if value > best_score:
            # Update the best score and key
            best_score = value
            best_key = key

    return best_key
