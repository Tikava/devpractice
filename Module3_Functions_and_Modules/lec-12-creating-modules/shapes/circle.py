import math

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    
    def get_area(self):
        return self.radius * self.radius * math.pi