import re
import time

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

try:
    print(a / b)
except ZeroDivisionError:
    print('Нельзя делать на ноль!')  
    
class ValidationError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
        
def contains_special_symbols(str):
    if re.search(r'[^a-zA-Z]', str):
        return True
    else:
        return False
        
name = input('Введите имя: ')
if contains_special_symbols(name) or len(name) == 0:
    raise ValidationError('Имя указано не верно', 100)


class Timer:
    def __enter__(self):
        self.start_time = round(time.time() * 1000)
        return self
    
    def __exit__(self, *args):
        self.end_time = round(time.time() * 1000)
        elapsed_time = self.end_time - self.start_time
        print(f"Execution time: {elapsed_time} milliseconds")
# measuring time
with Timer():
    for _ in range(10000):
        pass


