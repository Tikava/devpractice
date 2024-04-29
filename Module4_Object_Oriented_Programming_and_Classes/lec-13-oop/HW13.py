class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def description(self):
        return f"Brand:{self.brand}, model:{self.model}, year:{self.year}"

bmw = Car('BMW', 'M5', 2019)
print(bmw.description())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def get_info(self):
        return f"Employee's name - {self.name}, age - {self.age}, salary - {self.salary}"
    

employee = Employee('Almat', 18, 10000)
print(employee.get_info())

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('Гав!')

class Cat(Animal):
    def speak(self):
        print('Мяу!')

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено {amount}. Текущий баланс: {self.balance}")
        else:
            print("Сумма для внесения должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Снято {amount}. Текущий баланс: {self.balance}")
        elif amount > self.balance:
            print("Недостаточно средств на счете.")
        else:
            print("Сумма для снятия должна быть положительной.")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Начислены проценты: {interest}. Текущий баланс: {self.balance}")
        
savings = SavingsAccount('123456789', balance=1000, interest_rate=5)
savings.deposit(200)
savings.withdraw(100)
savings.add_interest()