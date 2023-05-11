#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]  # exclude the first element, which is the name of the script

    n_args = len(args)

    if n_args == 0:
      print('0 arguments.')
      print('.')
   else:
      print('{} argument{}:'.format(n_args, '' if n_args == 1 else 's'))
      for i, arg in enumerate(args):
          print('{}: {}'.format(i+1, arg))
