
my_list = input("Enter a list : ").split()
my_list = list(map(int, my_list))

minimum = my_list[0]

# print(min(my_list))
for i in my_list:
    if i < minimum:
        minimum = i

print(f"Smallest number : {minimum}")
