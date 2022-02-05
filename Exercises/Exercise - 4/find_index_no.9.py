
tup = tuple(input("Enter a tuple : ").split())

item = input("Enter an item : ")

if item not in tup:
    print("Item does not exit in tuple.")
else:
    print(f"Item found at index : {tup.index(item)}")
