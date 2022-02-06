
choice = input("True or False : ")

if choice.lower() == "true":
    num_of_lines = int(input("Enter number of lines : "))
    f = open("print_star.txt", "w")
    for i in range(1, num_of_lines + 1):
        for j in range(i):
            f.write("* ")
        f.write("\n")
    f.close()

else:
    num_of_lines = int(input("Enter number of lines : "))
    f = open("print_star.txt", "w")
    for i in range(num_of_lines + 1):
        for j in range(num_of_lines - i):
            f.write("* ")
        f.write("\n")
    f.close()
