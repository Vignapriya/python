n = int(input("enter the range:"))
for i in range(1, n+1):
   for s in range(n-1, i-1, -1):
      print(" ", end="")
   for j in range(1, i+1):
      print("* ", end="")
      print()
for i in range(1, n):
   for s in range(1, i+1):
      print(" ", end="")
   for j in range(n-1, i-1, -1):
      print("* ", end="")
      print()
