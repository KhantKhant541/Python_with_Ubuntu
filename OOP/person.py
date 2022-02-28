

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I am {self.name} and I am {self.age} years old."

    class DOB:
        def __init__(self):
            self.date = "1"
            self.month = "1"
            self.year = "2011"


p1 = Person("KPP", "18").DOB()
print(p1.year)
