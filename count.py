str1 = input("enter a string: ")
count = {}

for char in str1:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)
