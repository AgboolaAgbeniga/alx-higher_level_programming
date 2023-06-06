#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
    n = 0
    for m in range(x):
        try:
            print(my_list[m], end="")
            n += 1
        except IndexError:
            break
    print()
    return n
=======
    count = 0
    try:
        iterator = iter(my_list)
        while count < x:
            element = next(iterator)
            print(element, end=" ")
            count += 1
    except StopIteration:
        pass
    
    print()  # Print a new line
    
    return count
>>>>>>> 8234ce661a1e1606a0cb5c9ba3779e0eff30dff1
