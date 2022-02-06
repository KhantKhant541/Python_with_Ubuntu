
a = b'5'
string1 = b"Hello I am Khant Khant!"
list1 = [1, 2,  3, 4, 5]

with open("hello.bin", "wb") as f:
    # f.write(a)
    # f.write(string1)
    f.write(bytearray(list1))

with open("hello.bin", "rb") as f:
    temp = f.read()
    # print(int(temp))
    # print(temp.decode())
    print(list(temp))
