
class Bank:
    cash = 100000000

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    @classmethod
    def borrow(cls, bank):
        amount = int(input("Amount : "))
        bank.add_cash(amount)
        cls.cash -= amount

    def deposit(self):
        pass

    def withdraw(self):
        pass


class KBZ(Bank):

    def __init__(self, name, branch):
        self.cash = None
        self.location = None
        super().__init__(branch=branch, name=name)

    def set_cash(self):
        self.cash = 2000000

    def set_location(self):
        self.location = "Mandalay"

    def add_cash(self, cash):
        self.cash += cash
    # def borrow(self):
    #     amount = int(input("Enter amount of cash : "))
    #     self.cash += amount
    #     Bank.cash -= amount

    def __str__(self):
        return f"Bank Name : {self.name}\nLocation : {self.location} and\nAvailable cash : {self.cash}"


b = KBZ("KBZ", 2)
b.set_cash()
b.set_location()
print(b)
Bank.borrow(b)
print(b)
print(Bank.cash)
