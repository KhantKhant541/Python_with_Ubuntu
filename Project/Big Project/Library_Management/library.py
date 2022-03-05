import pickle

from book import Book
from logs import write_data, read_data

with open("Library-books.dat", "a")as f:
    pass

with open("Borrowed-books.dat", "a")as f1:
    pass


class Library:
    available_books = read_data("Library-books")
    borrowed_books = read_data("Borrowed-books")

    def __init__(self):
        self.name = None
        self.location = None

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    @staticmethod
    def borrow():
        name = input("Enter the book name : ")
        for i in range(len(Library.available_books)):
            if Library.available_books[i].get_title().lower() == name.lower():
                print("You may borrow a book.")
                temp = Library.available_books[i]
                Library.borrowed_books.append(Library.available_books[i])
                Library.available_books.remove(Library.available_books[i])
                with open("Library-books.dat", "wb")as f2:
                    for book in Library.available_books:
                        pickle.dump(book, f2)

                with open("Borrowed-books.dat", "wb")as f3:
                    for book in Library.borrowed_books:
                        pickle.dump(book, f3)

                return temp

        else:
            print("Sorry, currently the book is not available in the library")

    @staticmethod
    def return_book():
        name = input("Enter the book name : ")
        for i in range(len(Library.available_books)):
            if Library.borrowed_books[i].get_title().lower() == name.lower():
                print("You may return the book.")
                temp = Library.borrowed_books[i]
                Library.available_books.append(Library.borrowed_books[i])
                Library.borrowed_books.remove(Library.borrowed_books[i])

                with open("Library-books.dat", "wb") as f4:
                    for book in Library.available_books:
                        pickle.dump(book, f4)

                with open("Borrowed-books.dat", "wb") as f5:
                    for book in Library.borrowed_books:
                        pickle.dump(book, f5)

                return temp
        else:
            print("Something Wrong! Please tryagain!")

    @staticmethod
    def add_book():
        add_b = Book()
        add_b.set_title(input("Enter the book name : "))
        add_b.set_author_name(input("Enter the author name : "))
        add_b.set_pub_date(input("Enter the publish date : "))
        add_b.set_no_of_page(input("Enter the number of pages : "))

        write_data(add_b, "Library-books")
        Library.available_books.append(add_b)
