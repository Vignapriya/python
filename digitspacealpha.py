str1 = input("Enter a string: ")

digits = 0
spaces = 0
alphabets = 0

for char in str1:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        alphabets += 1
    elif char.isspace():
        spaces += 1

print("Number of digits:", digits)
print("Number of alphabets:", alphabets)
print("Number of spaces:", spaces)str1 = input("Enter a string: ")

