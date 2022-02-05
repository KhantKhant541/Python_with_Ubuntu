
tup = tuple(input("Enter a tuple : ").split())

tup_list = list(tup)

repeat_item = []
for item in tup_list:
    if tup.count(item) > 1 and item not in repeat_item:
        repeat_item.append(item)

tup = tuple(repeat_item)

print(f"Repeated items : {tup}")
