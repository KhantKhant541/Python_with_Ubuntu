
num = int(input("Enter positive integer : "))
sum = 0

while num > 0 and num % 2 == 0:
    sum = sum + num
    num = int(input("Enter positive integer : "))

if num % 2 != 0:
    print(f"Total sum : {sum}")
