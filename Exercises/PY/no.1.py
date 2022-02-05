# no.1
#
# print("First 10 natural numbers : ", end="")
#
# i = 1
# while i < 11:
#     print(i, end=" ")
#     i += 1

# no.2

# for i in range(5):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print("")

# no.3

# num = int(input("Enter a number : "))
# sum = 0
# for i in range(num+1):
#     sum += i
# print(f"Total sum up to {num} : {sum}")

# no.4

# num = int(input("Enter a number : "))
#
# print(f"Multiplication table of {num} : ")
# for i in range(1,11):
#     result = num * i
#     print(f"{num} x {i} = {result}")

# no.5

# list1 = list(map(int, input("Enter a list : ").split()))
#
# for item in list1:
#     if item > 500:
#         break
#     elif item % 5 == 0 and item <= 150:
#         print(item)
#     else:
#         continue

# no.6

# numb = int(input("Enter a number : "))
# count = 0
# digit = 0
#
# print(f"Number of digit in {numb} : ", end="")
# while numb > 1:
#     digit = numb % 10
#     count += 1
#     numb = numb / 10
#
# print(count)

# no.7

# row = int(input("Enter number of row  : "))
#
# for i in range(0, row+1):
#     for j in range(row - i, 0, -1):
#         print(j, end=" ")
#
#     print("")

# no.8

# list1 = list(map(int, input("Enter a list : ").split()))
#
# for item in list1[::-1]:
#     print(item)

# no.9

# for i in range(-10, 0):
#     print(i)

# no.10

# numb = int(input("Enter a number : "))
#
# for i in range(numb):
#     print(i)
#
# else:
#     print("Done!")

# no.11

# print("Please set a range.")
# start = int(input("Start point : "))
# end = int(input("End point : "))
#
# print(f"Prime number between {start} and  {end} are : ")
# count = 0
# for i in range(start, end):
#     for j in range(2, int(i/2)+1):
#         if i % j == 0:
#             count += 1
#     if count > 0:
#         count = 0
#     else:
#         print(i)

# no.12

# first = 0
# second = 1
# fibo = 0
#
# print(first, second, end=" ")
# for i in range(8):
#     fibo = first + second
#     first = second
#     second = fibo
#     print(fibo, end=" ")

# no.13

# numb = int(input("Enter an integer : "))
# factorial = 1
#
# # for i in range(1, numb+1):
# for i in range(numb, 0, -1):
#     factorial *= i
#
# print(f"{numb}! : {factorial}")

# no.14

# numb = int(input("Enter an integer : "))
# reverse = 0
#
# print(f"Reverse of {numb} : ", end="")
# while numb > 0:
#
#     reverse = reverse + (numb % 10)
#     numb = int(numb / 10)
#     if numb == 0:
#         break
#     reverse = reverse * 10
#
# print(reverse)

# no.15

# list1 = list(map(int, input("Enter a list : ").split()))
#
# for i in range(len(list1)):
#     if i % 2 != 0:
#         print(list1[i], end=" ")

# no.16

# numb = int(input("Enter an integer : "))
#
# for i in range(1, numb+1):
#     result = 1
#     for j in range(3):
#         result *= i
#
#     print(f"Current Number is : {i}  and the cube is : {result}")

# no.17

# numb = int(input("Enter number of terms : "))
#
# result = 0
# for i in range(numb):
#     term = 2
#     for j in range(i):
#         term = (term * 10) + 2
#     result = result + term
#
# print(result)

# no.18
#
# n = int(input("Enter number of line : "))
#
# for i in range(n+1):
#     for j in range(i):
#         print("* ", end="")
#     print("")
#
# for k in range(n-1, 0, -1):
#     for m in range(k):
#         print("* ", end="")
#     print("")

# Homework

tuple1 = tuple(map(int, input("Enter a tuple : ").split()))
print(f"You can slice between 1 and {len(tuple1) : }")

start, end = tuple(map(int, input("Enter start point and end point : ").split()))
while True:
    if start > 1 and end > 1:
        break
    else:
        print(f"Please enter between 1 and {len(tuple1)} only")
        start, end = tuple(map(int, input("Enter start point and end point : ").split()))
if start == end:
    print(tuple1[start])
else:
    for i in range(start, end):
        print(tuple1[i-1], end=" ")
    print()
