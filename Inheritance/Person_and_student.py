

class Person:
    def __init__(self):
        self.name = None
        self.age = None

    def __str__(self):
        return f"I am {self.name} and I am {self.age} years old."


class Student(Person):
    pass


s = Student()
s.name = "KK"
s.age = "18"
print(s)
