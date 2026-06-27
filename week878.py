


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number

        self.__balance = balance

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount
        return self.__balance

account = BankAccount("12345", 10000)
print(account.check_balance())
account.deposit(500)
print(account.check_balance())


from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass  

class Lion(Animal):
    def speak(self):
        return "Roar!"
    
    def move(self):
        return "Lion is running."
    
class Penguin(Animal):
    def speak(self):
        return "Hoot!"

    def move(self):
        return"Penguin is waddling."    
    

class Elephant(Animal):
    def speak(self):
        return "Trumpet!"
    
    def move(self):
        return "Elephant is stomping."
    
simba = Lion("Simba")
skipper = Penguin("Skipper")
dumbo = Elephant("Dumbo")

animals = [simba, skipper, dumbo]

for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")
    print(f"{animal.name} moves: {animal.move()}")



