import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I am {self.name} and I am {self.age} years old."


p = Person("KPP", 18)
with open("serialization.dat", "wb")as f:
    pickle.dump(p, f)
