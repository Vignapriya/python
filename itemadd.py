items = []

while True:
    val = raw_input("Enter item (or 'stop'): ")
    if val.lower() == "stop":
        break
    items.append(val)

result = tuple(items)
