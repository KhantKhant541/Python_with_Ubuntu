
my_list = input("Enter a list : ").split()
my_list = list(map(int, my_list))
multiply = 1

for i in my_list:
    multiply *= i

print(f"Multiplication of all items : {multiply}")
