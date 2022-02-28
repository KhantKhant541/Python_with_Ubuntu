
with open("account_info.txt", "a") as f:
    pass

with open("account_info.txt", "r") as file:
    data = file.readlines()
# print(data)
key = []
value = []
for item in data:
    data1 = item.strip("\n")
    data2 = data1.split(" : ")
    # print(data1)
    # print(data2)
    key.append(data2[0])
    value.append(data2[1])
# print(key, value)
dictionary_info = dict(zip(key, value))
# print(dictionary_info)


def create_account():
    name = input("Enter your full name : ")
    username = input("Enter username : ")
    password = input("Enter password : ")

    if username not in dictionary_info.values():
        with open("account_info.txt", "a+") as write_info:
            write_info.write(f"Name : {name}\nUsername : {username}\nPassword : {password}\n")


def login():
    username = input("Enter your username : ")
    password = input("Enter your password : ")

    if username not in dictionary_info.values():
        print("Your username doesn't exit.\n")
        choice = input("Do you want to create an account[Yes/no] : ")
        if choice.lower() == 'yes':
            create_account()
        else:
            print("Have a nice day.\nGet out quickly!\n")

    else:
        if username == dictionary_info['Username'] and password == dictionary_info['Password']:
            print("You have successfully logged in to your account.")
        else:
            print("Your username or password is incorrect!")


if __name__ == '__main__':
    choose = input("Do you want to create an account or log in? [Log in/create] : ")
    if choose.lower() == "log in":
        login()
    elif choose.lower() == "create":
        create_account()
    else:
        print("Invalid choice!\nPlease try again.\n")
