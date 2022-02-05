
tup = tuple(input("Enter a tuple : ").split())

tup_l = list(tup)

tup_l.remove(tup[0])
tup_l.remove(tup[4])
tup_l.remove(tup[5])

tup = tuple(tup_l)

print(f"After removing 0th, 4th and 5th : {tup}")

