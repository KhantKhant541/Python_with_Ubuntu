
my_list = input("Enter string list : ").split()

count = 0
for i in my_list:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1

print("Count : ", count)
