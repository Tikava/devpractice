from abc import ABC, abstractmethod

class Vehicle:
    
    def __init__(self, model, year):
        self.model = model
        self.year = year
        
class Car(Vehicle):

    def __init__(self, model, year, fuel_type):
        super().__init__(model, year)
        self.fuel_type = fuel_type
        
    def __str__(self):
        return f'Model - {self.model}\nYear - {self.year}'
        
vehicle = Vehicle('M8', 2023)
car = Car('M5', 2019, 'gasoline')
print(car)


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Animal, Flyable):
    def make_sound(self):
        return "Chirp chirp!"
    
    def fly(self):
        return "The bird is flying."
    
bird = Bird()
print(bird.make_sound())
print(bird.fly())

class Toyota(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficiency):
        super().__init__(model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficiency = fuel_efficiency
    
    def display_info(self):
        return f"Toyota {self.model_name}, Model: {self.model}, Year: {self.year}, Fuel Efficiency: {self.fuel_efficiency}"

class Ford(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficiency):
        super().__init__(model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficiency = fuel_efficiency
    
    def display_info(self):
        return f"Ford {self.model_name}, Model: {self.model}, Year: {self.year}, Fuel Efficiency: {self.fuel_efficiency}"

class Tesla(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficiency):
        super().__init__(model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficiency = fuel_efficiency
    
    def display_info(self):
        return f"Tesla {self.model_name}, Model: {self.model}, Year: {self.year}, Fuel Efficiency: {self.fuel_efficiency}"

toyota_car = Toyota('Corolla', 2021, 'Gasoline', 'Corolla', '30mpg')
ford_car = Ford('Mustang', 2020, 'Gasoline', 'Mustang GT', '15mpg')
tesla_car = Tesla('Model S', 2022, 'Electric', 'Model S Plaid', '102mpg equivalent')

print(toyota_car.display_info(), ford_car.display_info(), tesla_car.display_info())
