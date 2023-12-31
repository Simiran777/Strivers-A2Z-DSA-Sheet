def oddeven(n: int):
  x = str(n)
  odd = 0
  even = 0
  i = 0
  while i in range(len(x)):
    if int(x[i]) % 2 == 0:
      even += int(x[i])
    else:
      odd += int(x[i])
    i += 1
  print(f"{even} {odd}")

n = input()
oddeven(n)