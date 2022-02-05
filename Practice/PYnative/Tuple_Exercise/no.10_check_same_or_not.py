
tuple1 = tuple(map(int, input("Enter a tuple : ").split()))
tuple2 = tuple1

for i in range(len(tuple1)):
    if tuple1[i] == tuple2[i]:
        print("True")
