def prime(a):
    is_prime = True
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break

    if is_prime == False:
        return 0
    else:
        return 1

n = int(input("Enter a no: "))
b = prime(n)
print(b)
