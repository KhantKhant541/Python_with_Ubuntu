
# str1 = input("Enter a string : ")
# str2 = str1[::-1]
# print(str2)

# no.2
# str1 = input("Enter a string : ")
#
# str2 = str1[::-1]
#
# if str1 == str2:
#     print("Palindrome!")
# else:
#     print("Not Palindrome!")

# no.3
# list1 = list(input("Enter a list : ").split())
# rotation = int(input("How many times you want to rotate : "))
# copy_li = list1.copy()
# for i in range(rotation+1):
#     for j in range(len(list1)):
#         result_li[j] = copy_li[i]

# no.4
# dic = {}
# for i in range(11):
#     dic1 = {input("Enter name : "): int(input("Enter mark : "))}
#     dic.update(dic1)
#
# for i in range(6):
#     print(dic)

# no.5

# n = int(input("Enter a number : "))
# reverse = 0
#
# while n > 0:
#     reverse = (reverse * 10) + (n % 10)
#     n = int(n / 10)
#
# print(reverse)

# no.1
# n = int(input("Enter number of rows : "))
#
# for i in range(n+1):
#     for j in range(i):
#         print(i+j, end=" ")
#     print()
