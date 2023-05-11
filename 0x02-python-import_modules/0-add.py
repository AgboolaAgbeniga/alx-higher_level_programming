#!/usr/bin/python3
if __name__ == "__main__":
    # importing the function from add_0.py
    from add_0 import add

    # assigning values to a and b
    a = 1
    b = 2

    # calling the add function with arguments a and b, and printing the result
    print('{} + {} = {}'.format(a, b, add(a, b)))

