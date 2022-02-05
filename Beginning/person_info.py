
name = input("Enter your name : ")

age = int(input("Enter your age : "))

gender = input("Male/Female : ")

address = input("Enter your address : ")

height = input("Enter your height : ")

ph_no = int(input("Enter your Phone Number : "))

print(f"I am {name}({gender}). My height is {height}. I am {age} years old. I live in {address}.\nContact Number : 0{ph_no}")

print("I am " + name + "(" + gender + "). My height is " + height + ". I am " + str(age) + " years old. I live in " + address + ".\nContact Number : 0" + str(ph_no))
