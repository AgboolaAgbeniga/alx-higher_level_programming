#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]  # exclude the script name from the arguments list

    result = 0
    for arg in args:
        result += int(arg)

    print(result)
