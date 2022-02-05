
num = int(input("Enter the number : "))

for i in range(1, 11, 1):
    for j in range(1, num+1, 1):
        print(f"{j} x {i} = {j * i}\t", end='')
    print("")
