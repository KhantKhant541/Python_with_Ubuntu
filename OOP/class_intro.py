

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self):
        print(f"I am {self.name}. I can speak.")

    def age_(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def gender_(self):
        print(f"I am {self.name} and I am a {self.gender}")


p1 = Person("KPP", 18, "boy")
p1.speak()
p1.age_()
p1.gender_()
