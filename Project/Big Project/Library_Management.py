import pickle

from Person import Person
from library import Library
from logs import write_data, read_data

with open("user-accounts.dat", "a") as f:
    pass

accounts = read_data("user-accounts")


def login():
    username = input("Enter username : ")
    password = input("Enter the password : ")

    for j in range(len(accounts)):
        if accounts[j].get_username() == username and accounts[j].get_password() == password:
            return True, accounts[j]

    else:
        return False


def refresh(person_):
    for j in range(len(accounts)):
        if accounts[j].get_username() == person_.get_username():
            accounts[j] = person_

    with open("user-accounts.dat", "wb")as f1:
        for account in accounts:
            pickle.dump(account, f1)


def signup():
    s = Person()
    s.set_name(input("Enter your name : "))
    s.set_age(input("Enter your age : "))
    s.set_contact_no(input("Enter your phone number : "))
    s.set_dob(input("Enter your date of birth : "))
    s.set_username(input("Which username you want to use : "))
    s.set_password(input("Enter the password : "))
    write_data(s, "user-accounts")

    print("Congratulations! You have successfully create an account.")

    global accounts
    accounts.append(s)
    return s


if __name__ == '__main__':
    lib = Library()
    lib.set_name("Khant Khant")
    lib.set_location("Mandalay")
    print(f"Welcome to {lib.get_name()} Library.")

    have_account = input("Do you already have an account? [Y/n] : ").lower()

    if have_account == 'y':
        login_status, person = login()
        if not login_status:
            print("Incorrect username or password! Please try again.")
            exit(-1)
    else:
        person = signup()
    print("You have successfully login to your account!")

    choice = input("What do you want to do ? [borrow/return/add] : ").lower()

    if choice == "borrow":
        book = lib.borrow()
        person.add_books(book)
        print(book)
        refresh(person)

    elif choice == "add":
        lib.add_book()

    elif choice == "return":
        book = lib.return_book()
        refresh(person)
        for i in range(len(person.book_collection)):
            if person.book_collection[i].get_title() == book.get_title():
                person.book_collection.remove(person.book_collection[i])
                break
        refresh(person)
