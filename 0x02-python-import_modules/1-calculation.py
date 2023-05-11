#!/usr/bin/python3

if __name__ == "__main__":
  from calculator_1 import add, sub, mul, div

  a = 10
  b = 5

  addition = add(a, b)
  subtraction = sub(a, b)
  multiplication = mul(a, b)
  division = div(a, b)

  print('The sum of {} and {} is {}'.format(a, b, addition))
  print('The difference between {} and {} is {}'.format(a, b, subtraction))
  print('The product of {} and {} is {}'.format(a, b, multiplication))
  print('The division of {} by {} is {}'.format(a, b, division))
