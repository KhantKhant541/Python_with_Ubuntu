
class Book:
    def __init__(self):
        self.name = None
        self.author = None
        self.no_of_pages = None

    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def set_no_of_pages(self, no_of_pages):
        self.no_of_pages = no_of_pages

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_no_of_pages(self):
        return self.no_of_pages


book = Book()
book.set_name("No Mercy")
book.set_author("Scarlet C")
book.set_no_of_pages(50)
print(book.get_name())
print(book.get_author())
print(book.get_no_of_pages())
