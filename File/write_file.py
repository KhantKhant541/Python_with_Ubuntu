
file = open("text.txt", "w")

input_text = input("Enter a string : ")
file.write(input_text)

# input_text = input("Enter a list : ").split(",")
# file.writelines(input_text)

file.close()
