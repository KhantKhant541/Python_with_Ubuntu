
f = open("hello.txt", "rt")

print(f.readline())
f.seek(0)
print(f.readline())
print(f.tell())

f.close()
