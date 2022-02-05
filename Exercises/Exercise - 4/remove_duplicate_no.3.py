
tup = tuple(input("Enter a tuple : ").split())

tup_l = list(tup)

print(f"Before removing duplicated item : {tuple(tup)}")

for item in tup:
    if tup_l.count(item) > 1:
        tup_l.remove(item)

tup = tuple(tup_l)
print(f"After removing duplicated item : {tup}")
