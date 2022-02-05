my_list = input("Enter a list : ").split()
my_list = list(map(int, my_list))

temp = my_list[0]

for i in my_list:
    if i > temp:
        temp = i

print("Maximum value in list : ", temp)

print(max(my_list))
