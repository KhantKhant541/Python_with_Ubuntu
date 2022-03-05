from Person import Person
from logs import *
from Library import Library

with open("User-accounts.dat", "a") as f:
    pass

accounts = read_data("User-accounts")


def login():
    user_name = input("Enter the username : ")
    password = input("Enter the password : ")

    for account in accounts:
        if account.get_username().lower() == user_name.lower() and account.get_password().lower() == password.lower():
            print("You have logged in successfully!")
            return account

    else:
        print("Wrong username or password!")


def create_account():
    name = input("Enter your name : ")
    age = input("Enter your age : ")
    contact = input("Enter your phone number : ")
    dob = input("Enter DOB : ")
    username = input("Enter the username : ")
    password = input("Enter the password : ")

    p = Person()
    p.set_name(name)
    p.set_age(age)
    p.set_dob(dob)
    p.set_contact(contact)
    p.set_username(username)
    p.set_password(password)

    write_data("User-accounts", p)
    accounts.append(p)
    return p


if __name__ == '__main__':
    my_lib = Library()
    my_lib.set_name("La Plu Ma")
    my_lib.set_address("Mandalay!")
    print(f"Welcome to {my_lib.name} Library!")
    choice = input("Do you have an account? [Y/n] : ").lower()
    person = None
    if choice == "y":
        person = login()
        if person is None:
            exit()

    elif choice == "n":
        person = create_account()

    # print(person.book_collection[0])
    choice = input("[Borrow / Add / Return] : ").lower()
    if choice == "borrow":

        book = my_lib.borrow_book()
        person.book_collection.append(book)

        books = person.get_collection()
        print("Books available in the library : ")
        for book_ in books:
            print(book_.get_title())

        book_to_read = input("Which book do you want to read : ")
        for book_ in books:
            if book_.get_title().lower() == book_to_read.lower():
                print(book_)
                break
            else:
                print("The book is not in your collection!")

        update_user(person)
        accounts = read_data("User-accounts")

    elif choice == "return":
        book = my_lib.return_book()
        for book_ in person.book_collection:
            if book_.get_title() == book.get_title():
                person.book_collection.remove(book_)
                break
        update_user(person)
        accounts = read_data("User-accounts")

    elif choice == "add":
        my_lib.add_book()
        update_user(person)
        print("You have successfully added the book to the library!")
