
tuple1 = tuple(map(int, input("Enter a tuple : ").split()))
element = int(input("Enter element : "))

print(f"Occurrence of {element} : {tuple1.count(element)}")
