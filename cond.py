str1 = input("Enter a string: ")

if len(str1) < 3:
    print(str1)
else:
    if str1.endswith("ing"):
        str1 = str1 + "ly"
    else:
        str1 = str1 + "ing"
    print(str1)
