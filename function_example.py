#!/bin/env python3
def square(x):
  y=x**2
  return y

def main():
  n=int(input('Enter a number: '))
  result=square(n)
  print('{1} is the square of {0}'.format(n,result))

if __name__ == '__main__':
  main()
