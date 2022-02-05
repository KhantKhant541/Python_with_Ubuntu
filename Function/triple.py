# def square(n):
#     total = n * 3
#
#     if total == 15 or total == 18:
#         return n
#     else:
#         return total
#
#
# num = list(map(int, input("Enter a number : ").split()))
#
# result = list(map(square, num))
# print(num)
# print(result)

li = list(map(int, input("Enter a list : ").split()))

square = list(map(lambda n: n ** 2, li))

print(square)
