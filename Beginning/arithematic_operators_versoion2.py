
a = int(input("Enter a positive integer : "))
b = 0

b += a
print(f"Addition  : {b}")

b = 0
b -= a
print(f"Subtraction : {b}")

b = 0
b *= a
print(f"Multiplication : {b}")

b = 0
b /= a
print(f"Division : {b}")

b = 0
b %= a
print("Modulus : ", b)

b = 0
b **= a
print("Exponent : ", b)

b = 0
b //= a
print("Floor Division : ", b)
