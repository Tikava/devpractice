import abc
import math

def add(a: [int, float, str], b: [int, float, str]) -> [int, float, str]:
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))) or \
        (isinstance(a, str) and isinstance(b, str)):
        return a + b  
    else:
        raise TypeError('Не поддерживаемые типы для сложения') 
def subtract(a : [int, float], b : [int, float]) -> [int, float]:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise TypeError('Не поддерживаемые типы для вычитания')
        
def multiply(a, b):
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))) or \
        (isinstance(a, str) and isinstance(b, int)):
        return a * b
    else:
        raise TypeError("Неподдерживаемые типы для операции умножения")
    
def divide(a: int, b: int) -> float:
    if isinstance(a, int) and isinstance(b, int):
        if b == 0:
            raise ValueError("Деление на ноль")
        return a / b
    else:
        raise TypeError("Неподдерживаемые типы для операции деления")
    
print(add('Привет ', 'мир'))
print(add(5, 2))
print(add(5.5, 2.2))


class Shape:
    
    def area(self):
        pass
    
class Triangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height / 2

class Drawable(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass

class Circle(Shape, Drawable):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def draw(self):
        print('    -----')
        print('  /        \\')
        print(' |          |')
        print('  \        /')
        print('    -----')

class Rectangle(Shape, Drawable):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        return self.a * self.b
    
    def draw(self):
        print('------')
        print('|    |')
        print('|    |')
        print('------')
        
shapes = [Circle(), Rectangle()]
for shape in shapes:
    shape.draw()