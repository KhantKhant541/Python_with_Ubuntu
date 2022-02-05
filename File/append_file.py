
file = open("hello.txt", "a")

text = input("Enter a string : ")

file.write(f"{text}\n")

file.close()
