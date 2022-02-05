from array import array
# no.1
# arr1 = array('i', [1, 2, 3, 4, 5])
# for i in range(3):
#     print(arr1[i])

# no.2
# arr1 = array('i', [1, 3, 5, 9])
# arr1.append(11)
# print(arr1)

# no.3
# arr1 = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# arr1.reverse()
# print(arr1)

# no.4
# arr1 = array('i', [1, 3, 5, 7, 9])
# print(arr1.itemsize)

# no.5
# arr1 = array('i', [1, 3, 5, 7, 9])
# buffer = arr1.buffer_info()
# print(buffer)
# print(buffer[1] * arr1.itemsize)

# no.6
# arr1 = array('i', [1, 3, 5, 3, 7, 9, 3])
# print(f"Occurrence of 3 in array : {arr1.count(3)}")

# no.7
# arr1 = array('i', [1, 3, 5, 7, 9])
# arr1.extend(arr1)
# print(arr1)

# no.8
# arr1 = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
# print(arr1.tobytes())

# no.9
# list1 = [1, 2, 6, -8]
# arr1 = array('i', [])
# arr1.fromlist(list1)
# print(arr1)

# no.10
# arr1 = array('i', [1, 3, 5, 7, 9])
# arr1.insert(1, 4)
# print(arr1)

# no.11
# arr1 = array('i', [1, 3, 5, 7, 9])
# arr1.remove(5)
# print(f"After removing 3rd element : {arr1}")

# no.12
# arr1 = array('i', [1, 3, 5, 3, 7, 1, 9, 3, 5, 7])
# arr1.remove(1)
# print(arr1)

# no.13
# arr1 = array('i', [1, 3, 5, 7, 9])
# print(arr1.tolist())

# no.14
# arr1 = array('i', map(int, input("Enter an array : ").split()))
# count = 1
# for i in range(len(arr1)):
#     for j in range(i+1, len(arr1)):
#         if arr1[i] == arr1[j]:
#             count += 1
# if count > 1:
#     print(True)
# else:
#     print(False)

# no.15
# arr1 = array('i', map(int, input("Enter an array : ").split()))
# count = 0
# for i in range(len(arr1)):
#     if count > 0:
#         break
#     else:
#         for j in range(i+1, len(arr1)):
#             if arr1[i] == arr1[j]:
#                 print(arr1[i])
#                 count += 1
#
# if count == 0:
#     print("-1")

# no.16


# no.17
# arr1 = array('i', map(int, input("Enter an array : ").split()))
# product = 1

# no.18
# arr1 = array('i', [])
# for i in range(6):
#     element = int(input(f"Enter element {i+1} : "))
#     arr1.append(element)
# for item in arr1:
#     print(item)

# no.19
# arr1 = array('i', map(int, input("Enter an array : ").split()))
# print(arr1.buffer_info())

# no.20
# arr1 = array('i', map(int, input("Enter an array : ").split()))
# print(len(arr1))

# no.21
# arr1 = array('I', [1, 2, 3])
# arr2 = array('f', [1.2, 2.3, 3.4])
# print(arr1.itemsize)
# print(arr2.itemsize)

# no.22
# arr1 = array('i', [1, 2, 3, 4, 5])
# print(arr1)
# to_byte = arr1.tobytes()
# print(f"In byte : {to_byte}")
# arr2 = array('i')
# arr2.frombytes(to_byte)
# print(arr2)

# no.23
# arr1 = array('i', map(int, input("Enter an array : ").split()))


# no.24

