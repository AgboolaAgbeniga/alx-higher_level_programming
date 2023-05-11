#!/usr/bin/python3

if __name__ == "__main__":
  from calculator_1 import add, sub, mul, div

  a = 10
  b = 5
  print('The sum of {} and {} is {}'.format(a, b, add(a, b)))
  print('The difference between {} and {} is {}'.format(a, b, sub(a, b)))
  print('The product of {} and {} is {}'.format(a, b, mul(a, b)))
  print('The division of {} by {} is {}'.format(a, b, div(a, b)))
