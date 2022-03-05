from book import Book
from logs import *

with open("Available_Books.dat", "a")as f:
    pass

with open("Borrowed_Books.dat", "a")as f1:
    pass


class Library:
    def __init__(self):
        self.name = None
        self.address = None
        self.available_books = []
        self.borrowed_books = []

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def refresh(self):
        self.available_books = read_data("Available_Books")
        self.borrowed_books = read_data("Borrowed_Books")

    def add_book(self):
        name = input("Enter book name : ")
        author = input("Enter author name : ")
        publish_date = input("Enter the publish date : ")
        no_of_pages = input("Enter number of pages : ")

        b = Book(name, author, publish_date, no_of_pages)
        self.available_books.append(b)
        write_data("Available_Books", b)
        self.refresh()

    def borrow_book(self):
        self.refresh()
        book = input("Enter Name of the book : ")

        for book_ in self.available_books:
            if book_.get_title().lower() == book.lower():
                self.borrowed_books.append(book_)
                self.available_books.remove(book_)

                remove_book("Available_Books", book_)
                write_data("Borrowed_Books", book_)

                print("You have successfully borrowed the book!")
                return book_

        else:
            print("The book is unavailable in the library!")
        self.refresh()

    def return_book(self):
        self.refresh()
        book = input("Enter Name of the book : ")

        for book_ in self.borrowed_books:
            if book_.get_title().lower() == book.lower():
                self.available_books.append(book_)
                self.borrowed_books.remove(book_)

                remove_book("Borrowed_Books", book_)
                write_data("Available_Books", book_)

                print("You have successfully returned the book!")
                return book_

        else:
            print("Something Wrong!")
        self.refresh()
