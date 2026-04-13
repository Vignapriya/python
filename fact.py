def fact(n):
    if n < 0:
        print("negative values invalid input")
    elif n == 0:
        print("factorial = 1")
    else:
        factorial = 1
        while n > 0:
            factorial = factorial * n
            n = n - 1
        print(factorial)
n1 = int(input("Enter a no: "))
fact(n1)
