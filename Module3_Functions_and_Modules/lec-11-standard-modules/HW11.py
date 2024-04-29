import math
import datetime
import random

def area_of_circle(radius):
    return math.pi * radius * radius

print(area_of_circle(5))

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(10))

def area_of_triangle(width, height):
    return 0.5 * width * height

def after_seven_days(date):
    return datetime.datetime(date.year, date.month, date.day + 7)

print(after_seven_days(datetime.datetime.now()))

def get_day_difference(first_date, second_date):
    return abs((second_date - first_date).days)

print(get_day_difference(after_seven_days(datetime.datetime.now()), datetime.datetime.now()))

def get_weekday(date):
    return date.strftime('%A')

print(get_weekday(datetime.datetime.now()))

def select_random():
    return random.randint(1, 6)

x = int(input('Загадай число от 1 до 6 (вкл.): '))
if (x == select_random()):
    print('Поздравляю! Вы выиграли')
else:
    print('Вы проиграли! Не расстраивайтесь')


def generate_random_name():
    length = random.choice(range(3, 10))
    name = ''
    for _ in range(length):
        name += random.choice([str(random.randint(0, 9)), chr(random.randint(1, 26) + 96)])
    return name

print(generate_random_name())


participants = ['Almat', 'Toilybay', 'Fedor', 'Anastasia', 'Meiirbek']
print('AND THE WINNER IS ........', random.choice(participants))

def current_time():
    now = datetime.datetime.now()
    for i in range(60):
        print(datetime.datetime(now.year, now.month, now.day, now.hour, (now.minute + (now.second + i) // 60) % 60, (now.second + i) % 60))

current_time()

def get_current_time(format = 1): # Has format options. Be default local format
    match format:
        case 1: #Local format
            return datetime.datetime.now().strftime('%H:%M:%S')
        case 2: #Non local format (AM/PM)
            return datetime.datetime.now().strftime('%I:%M:%S %p')
print(get_current_time(2))
print(get_current_time())


def get_random_time():
    year = random.randrange(1, 9999)
    month = random.randrange(1, 12)
    day = random.randrange(1, 31)
    hour = random.randrange(0, 23)
    minute = random.randrange(0, 59)
    second = random.randrange(0, 59)
    return datetime.datetime(year, month, day, hour, minute, second).strftime('%c')
print(get_random_time())