
numb = int(input("Enter number of tuple : "))

tuple_list = []
for i in range(numb):
    tuple1 = tuple(map(int, input(f"Enter tuple {i+1} : ").split()))
    tuple_list.append(tuple1)

result_list = []
copy_list = tuple_list.copy()
copy_tup = ()
for item in tuple_list:
    temp = copy_list[0][-1]
    for i in copy_list:
        if i[-1] < temp:
            copy_tup = i

result_list.append(copy_tup)
copy_list.remove(copy_tup)

print(result_list)
