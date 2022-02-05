
file = open("hello.txt", "a+")

text = file.read()
print(text)

append_text = input("Enter a string : ")
file.write(append_text)

file.close()

