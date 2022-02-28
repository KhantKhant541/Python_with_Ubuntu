
class Animal:
    no_of_animal = 0

    def __init__(self):
        self.name = None
        self.types = None
        Animal.no_of_animal += 1

    def set_animal_name(self, name):
        self.name = name

    def set_types(self, types):
        self.types = types

    def get_name(self):
        return self.name

    def get_types(self):
        return self.types

    def __str__(self):
        return f"Name : {self.get_name()}, Type : {self.get_types()}"

    @classmethod
    def get_no_of_animal(cls):
        return cls.no_of_animal


animal = Animal()
animal.set_animal_name("Dog")
animal.set_types("Land Animal")

animal_2 = Animal()
animal_2.set_animal_name("Fish")
animal_2.set_types("Aquarius")

print(animal.get_name())
print(animal.get_types())

print(animal_2.get_name())
print(animal_2.get_types())

print(f"Number of Animals : {Animal.get_no_of_animal()}")

print(animal)
print(animal_2)


