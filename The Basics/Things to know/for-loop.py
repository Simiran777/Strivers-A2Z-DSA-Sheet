# Nth Fibonacci Number
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def fibo(x: int):
  mylist = [1,1]
  if x == 0:
      return 0
  elif x == 1 or x == 2:
      return 1
  else:
      n = 2
      for n in range(2,x+1):
        a = mylist[n-1] + mylist[n-2]
        mylist.append(a)
        n += 1
      return mylist[x-1]

x = int(input())
print(fibo(x))