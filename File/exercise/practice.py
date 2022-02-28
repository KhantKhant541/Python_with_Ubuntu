
# no.1

# char = input("Enter a character : ")
# with open("test_file.txt", "w") as f:
#     f.write(char)

# no.2

# method 1
# try:
#     with open("test_file.txt", "r")as f:
#         print(f.read())
#
# except FileNotFoundError:
#     print("File does not exit!")

# method 2
# import os
#
# if os.path.exists("test_file.txt"):
#     print("File is found!")
# else:
#     print("File is not found!")

# no.3

# string1 = """Hello how are you?
# I Hope you are well.
# I am Khant Khant!"""
# with open("test.txt", "w")as f:
#     f.write(string1)

# no.4

# with open("test.txt", "rt")as f:
#     print(f.read())

# no.5

# name = input("Enter name : ")
# ph_number = int(input("Enter phone number : "))
# with open("test.txt", "a") as f:
#     f.write(f"Name : {name}\n")
#     f.write(f"Phone Number : 0{ph_number}\n")

# no.6

word = 0
char = 0
with open("test.txt", "rt") as f:
    file = f.readlines()
    print(f"Lines : {len(file)}")
    for lines in file:
        word += len(lines.split(" "))
    print(f"Words : {word}")
    for lines in file:
        char += len(lines)
    print(f"Characters : {char}")
    # print(file)

# no.7

# append_data = input("Enter everything you want to append to a file : ")
# with open("test.txt", "a+") as f:
#     f.write(f"{append_data}\n")
#     f.seek(0)
#     print(f.read())

# no.8

# with open("anime-anime-girls-digital-art-artwork-2d-hd-wallpaper-preview.jpg", 'rb')as f:
#     temp = f.read()
#
# with open("copy_photo.jpg", 'wb') as f1:
#     f1.write(temp)

# no.9

# with open("test.txt", "w") as f:
#     f.write("Hello, How are you.\nI hope you are well.\nAs for me, I am fine.")

# no.10

# with open("test.txt", "rt") as f:
#     test = f.read()
#     print(test)

# no.11

# a, b, c = b'10', b'20', b'30'
# with open("test.bin", "wb") as f:
#     f.write(a)
#     f.write(b)
#     f.write(c)

# no.12

# city_name = input("Enter the city name and the first letter in upper case : ")
# with open("city.txt", "rt") as f:
#     name = f.readlines()
#     print(name)
#     for city in name:
#         if city_name in city:
#             print(f"{city_name}is recorded at position {city[0]}")

# no.13

# str1 = b'Why are you Gay?'
# with open("test.bin", "wb") as f:
#     f.write(str1)

# no.14

# with open("test.bin", "wb") as f:
#     pass
