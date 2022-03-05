
class Father:
    def __init__(self, name):
        self.name = name
        self.property = 80000

    def display_property(self):
        print(self.property)

    def __str__(self):
        return f"Name is {self.name} and property is {self.property}"


class Son(Father):

    def __init__(self):
        name = "KK"
        super().__init__(name)
        super().display_property()


s = Son()
print(s)
