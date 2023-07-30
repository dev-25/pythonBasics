
# Encapsulation in Python is achieved by bundling data and methods within a single unit, known as a class. 
# This concept helps to protect the data and methods from outside interference, as it restricts direct access to them.
# Two ways to achive Encapsulation
# 1 -> Using private members: Cannot be accessed outside the class and subclasses (__hello).
# 2 -> Using protected members: Can be assessed in subclass (_hello)


# Code 1 -> Using Private members
class BankAccount:  
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)   # Crating an object -> account 
account.deposit(100)
print(account.get_balance())  # 1100
account.withdraw(500)
print(account.get_balance())  # 600


# Code 2
class BankAccount:  
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self):
        return self._balance

class Devesh(BankAccount):
    def __init__(self, ACC_balance):
        super().__init__(ACC_balance)

account = Devesh(2000)
account.deposit(100)
print(account.get_balance())  # 2100
account.withdraw(500)
print(account.get_balance())  # 1600