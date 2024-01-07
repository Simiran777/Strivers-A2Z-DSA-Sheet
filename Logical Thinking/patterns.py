"""
Example  * * *
         * * *
         * * *
"""
def pattern(n: int):
  for i in range(n):
    for j in range(n):
      print("*", end =" ")
    print(end = "\n")

n = int(input())
pattern(n)

"""
Example  * 
         * * 
         * * *
"""
def pattern(n: int):
  for i in range(1,n+1):
    print("* " * i)

n = int(input())
pattern(n)

"""
Example  1 
         1 2 
         1 2 3
"""
def pattern(n: int):
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(j, end=" ")
    print(end = "\n")

n = int(input())
pattern(n)

"""
Example  1 
         2 2 
         3 3 3
"""
def pattern(n: int):
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(i, end=" ")
    print(end = "\n")

n = int(input())
pattern(n)

"""
Example  * * * 
         * *
         *
"""
def pattern(n: int):
  for i in reversed(range(1,n+1)):
    print("* " * i)

n = int(input())
pattern(n)

"""
Example  1 2 3 
         1 2 
         1
"""
def pattern(n: int):
  for i in reversed(range(1,n+1)):
    for j in range(1,i+1):
      print(j, end=" ")
    print(end = "\n")

n = int(input())
pattern(n)

""" Example   *
             ***
            *****          
"""
def pattern(n: int):
  list1=[]
  for i in range(0,n*2):
    if i % 2 != 0:
      list1.append(i)
  for k in range(len(list1)):
    print(" " * (n-k-1) , end="")
    print("*" * list1[k])


n = int(input())
pattern(n)

"""Example  *****
             ***
              *
"""
def pattern(n: int):
  list1=[]
  for i in range(0,n*2):
    if i % 2 != 0:
      list1.append(i)
  for k in reversed(range(len(list1))):
    print(" " * (n-k-1) , end="")
    print("*" * list1[k])


n = int(input())
pattern(n)

""" Example   *
             ***
            *****
            *****
             ***
              *
"""
def pattern(n: int):
  list1=[]
  for i in range(0,n*2):
    if i % 2 != 0:
      list1.append(i)
  for k in range(len(list1)):
    print(" " * (n-k-1) , end="")
    print("*" * list1[k])
  for k in reversed(range(len(list1))):
    print(" " * (n-k-1) , end="")
    print("*" * list1[k])

n = int(input())
pattern(n)

""" Example *
            **
            ***
            ****
            *****
            ****
            ***
            **
            *
"""
def pattern(n: int):
  list1=[]
  for i in range(1,n+1):
    list1.append(i)
  for j in range(len(list1)):
    print("*" * list1[j])
  list1.reverse()
  for j in range(1,len(list1)):
    print("*" * list1[j])

n = int(input())
pattern(n)

""" Example 1 
            0 1
            1 0 1
"""
def pattern(n: int):
  for i in range(1,n+1):
    for j in reversed(range(1,i+1)):
      a = 0 if j%2==0 else 1
      print(a, end=" ")
    print(end="\n")

n = int(input())
pattern(n)

""" Example  1         1
             1 2     2 1
             1 2 3 3 2 1
"""
def pattern(n: int):
    mylist = []
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for k in reversed(range(n)): 
            mylist.append(k)
        a = (n+1) * mylist[i-1]
        print(" " * a,end="")
        for j in reversed(range(1,i+1)):
            print(j,end=" ")
        print(end="\n")

n = int(input())
pattern(n)

""" Example 1
            2 3
            4 5 6
"""
def pattern(n: int):
  count = 1
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(count, end =" ")
      count += 1
    print(end="\n")

n = int(input())
pattern(n)

""" Example A
            A B
            A B C
"""
def pattern(n: int):
  count = 65
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(chr(count), end =" ")
      count += 1
    count = 65
    print(end="\n")

n = int(input())
pattern(n)

""" Example A B C
           A B
           A
"""
def pattern(n: int):
  count = 65
  for i in reversed(range(1,n+1)):
    for j in reversed(range(1,i+1)):
      print(chr(count), end =" ")
      count += 1
    count = 65
    print(end="\n")

n = int(input())
pattern(n)

""" Example A 
           B B
           C C C
"""
def pattern(n: int):
  count = 65
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(chr(count), end =" ")
    count += 1
    print(end="\n")

n = int(input())
pattern(n)

""" Example    A
             A B A
            A B C B A
"""
def pattern(n: int):
  count = 65
  for i in range(n):
    for j in range(n-i-1):
      print(" ", end="")
    if count >= 65:
      for x in range(65,count+1):
        print(chr(x), end = " ")
      for x in reversed(range(65,count)):
        print(chr(x), end = " ")
      count += 1
    for j in range(n-i-1):
      print(" ", end="")
    print(end="\n")

n = int(input())
pattern(n)

""" Example C
            C B
            C B A
"""
def pattern(n: int):
  for i in range(n):
    for j in range(i+1):
      print(chr(64+n-j),end=" ")
    print(" ")

n = int(input())
pattern(n)

""" Example ******
           **  **
           *    *
           *    *
           **  **
           ******
"""
def pattern(n: int):
  mylist = []
  for i in range(2*n):
    if i % 2 == 0:
      mylist.append(i)
  for i in range(n):
    print("* " * (n-i),end="")
    print(" " * 2 * mylist[i],end="")
    print("* " * (n-i),end="")
    print("")
  for i in reversed(range(n)):
    print("* " * (n-i),end="")
    print(" " * 2 * mylist[i],end="")
    print("* " * (n-i),end="")
    print("")

n = int(input())
pattern(n)

""" Example*         *
           * *     * *
           * * * * * *
           * *     * *
           *         *
"""
def pattern(n: int):
  mylist = []
  for i in range(2*n):
    if i % 2 == 0:
      mylist.append(i)
  for i in reversed(range(n)):
    print("* " * (n-i),end="")
    print(" " * 2 * mylist[i],end="")
    print("* " * (n-i),end="")
    print("")
  for i in range(1,n):
    print("* " * (n-i),end="")
    print(" " * 2 * mylist[i],end="")
    print("* " * (n-i),end="")
    print("") 

n = int(input())
pattern(n)

""" Example ***
            * *
            ***
"""
def pattern(n: int):
  if n > 1:
    print( "*" * n)
    for i in range(n-2):
        print("*",end="")
        print(" " * (n-2),end="")
        print("*")
    print( "*" * n)
  else:
    print("*", end="")
  
n = int(input())
pattern(n)