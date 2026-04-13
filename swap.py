def swap(x, y):
    x = x + y
    y = x - y
    x = x - y
    print("After swapping =", x, y)

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
swap(a,b)
