
my_list = input("Enter a list : ").split()
my_list = list(map(int, my_list))

sum = 0

for i in my_list:
    sum += i

print(f"Sum of all items : {sum}")
