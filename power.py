def power(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        c = a ** b
        return c

d = power(5, 2)
print(d)
