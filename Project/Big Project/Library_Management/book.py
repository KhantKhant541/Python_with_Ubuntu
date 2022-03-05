
class Book:
    def __init__(self):
        self.title = None
        self.author_name = None
        self.pub_date = None
        self.no_of_pages = None

    def set_title(self, name):
        self.title = name

    def set_author_name(self, author_name):
        self.author_name = author_name

    def set_pub_date(self, date):
        self.pub_date = date

    def set_no_of_page(self, pages):
        self.no_of_pages = pages

    def get_title(self):
        return self.title

    def get_author_name(self):
        return self.author_name

    def get_pub_date(self):
        return self.pub_date

    def get_no_of_pages(self):
        return self.no_of_pages

    def read(self):
        return f"Title : {self.title}\nAuthor : {self.author_name}\nPublish Date : {self.pub_date}"

    def __str__(self):
        return f"Title : {self.title}\nAuthor : {self.author_name}\nPublish Date : {self.pub_date}"
