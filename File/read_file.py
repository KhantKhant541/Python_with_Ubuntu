
file = open("hello.txt", "r")

text = file.read()
# text = file.readline()
# text = file.readlines()

print(text)

file.close()
