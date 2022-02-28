

class Book:
    def __init__(self, name, author, page, price):
        self.name = name
        self.author = author
        self.page = page
        self.price = price

    def read(self):
        print(f"Book name : {self.name}, Author : {self.author}")

    def getNumPages(self):
        print(f"Book name is {self.name} and it has  {self.page} pages")

    def get_book_price(self):
        print(f"Book name is {self.name} and its price is {self.price}")

    def __str__(self):
        return f"Book Name : {self.name}, Author : {self.author}"


b1 = Book("A Silent Night", "Jough", 225, "10k Ks")
b1.read()
b1.getNumPages()
b1.get_book_price()
print(b1)
