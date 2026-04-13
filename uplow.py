def uplow(str1):
    upc=0
    loc=0
    upchar=" "
    lowchar=" "
    for char in str1:
        if char.isupper():
            upc+=1
            upchar+=char
        if char.islower():
            loc+=1
            lowchar+=char
    print("upper case:")
    print(upc)
    print(upchar)
    print("lower case:")
    print(loc)
    print(lowchar)
str1=input("enter a string: ")
print("original string: ",str1)
uplow(str1)
