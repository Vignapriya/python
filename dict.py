def add_key_to_dictionary(d):
    key = raw_input("Enter key to add: ")
    value = int(input("Enter value: "))
    d[key] = value
my_dict = { 'apple': 50, 'banana': 20, 'cherry': 40 }

print("Original Dictionary:")
print(my_dict)

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("\nDictionary sorted by value:")
print(sorted_dict)

add_key_to_dictionary(my_dict)

print("\nDictionary after adding new key:")
print(my_dict)
