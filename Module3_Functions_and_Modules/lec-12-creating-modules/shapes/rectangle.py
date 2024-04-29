class Rectangle:
    def __init__(self, a, b, c):
        if (a + b > c and b + c > a and a + c > b):
            self.a = a
            self.b = b
            self.c = c
        return "Can't construct rectangle"
    
    def __str__(self):
        return f"a={self.a}, b={self.b}, c={self.c}"