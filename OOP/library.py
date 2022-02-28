
class Library:
    def __init__(self):
        self.name = None
        # self.time = None
        self.address = None
        self.no_of_book = None

    def set_name(self, name):
        self.name = name

    def set_time(self, open_time, close_time):
        self.open_time = open_time
        self.close_time = close_time

    def set_address(self, address):
        self.address = address

    def set_no_of_book(self, no_of_book):
        self.no_of_book = no_of_book

    def get_name(self):
        return self.name

    def get_time(self):
        return self.open_time, self.close_time

    def get_address(self):
        return self.address

    def get_no_of_book(self):
        return self.no_of_book

    def borrow_book(self):
        print("You have successfully borrow a book.")

    def return_book(self):
        print("You have successfully return a book.")


lib = Library()
lib.set_name("Khant Khant")
lib.set_address("Mandalay")
lib.set_time("6 A.M", "6 P.M")
lib.set_no_of_book(30)
print(lib.get_name())
print(lib.get_address())
print(lib.get_time())
print(lib.get_no_of_book())
lib.borrow_book()
lib.return_book()
