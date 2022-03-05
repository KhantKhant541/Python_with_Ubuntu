

class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.contact_no = None
        self.dob = None
        self.username = None
        self.password = None
        self.book_collection = []

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_contact_no(self, contact):
        self.contact_no = contact

    def set_dob(self, dob):
        self.dob = dob

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def add_books(self, book):
        self.book_collection.append(book)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_books(self):
        return self.book_collection

    def read(self):
        book_name = input("Which book do you want to read? : ")
        for i in range(len(self.book_collection)):
            if self.book_collection[i].get_title().lower == book_name.lower():
                print(self.book_collection[i].read())

    def __str__(self):
        print(f"I am {self.name}")
