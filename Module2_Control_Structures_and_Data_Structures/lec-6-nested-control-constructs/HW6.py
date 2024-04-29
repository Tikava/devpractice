import math

grade = int(input())
if grade >= 1 and grade <= 3:
    print('Плохо')
elif grade >= 4 and grade <= 6:
    print('Удовлетворительно')
elif grade >= 7 and grade <= 9:
    print('Хорошо')
else:
    print('Отлично')

currentHour = int(input())
if currentHour >= 6 and currentHour < 12:
    print('Доброе утро')
elif currentHour >= 12 and currentHour < 18:
    print('Добрый день')
elif currentHour >= 18 and currentHour <= 23:
    print('Добрый вечер')
elif currentHour >= 0 and currentHour < 6:
    print('Спокойной ночи')

number = int(input())
for i in range(1, number):
    if i % 3 == 0:
        print(i)

list = [1, 0, -10, 4, 2, 10, -4]
sum, size = 0, 0
for item in list:
    if item > 0:
        sum += item
        size += 1
print('Avg', sum / size)

height = int(input('Введите высоту елочки: '))
width = 2
x = height
for i in range(height):
    for j in range(x - 1):
        print(" ", end="")
    x -= 1
    for j in range(1, width):
        if j % 2 == 1:
            print("*", end="")
        else: 
            print(" ", end="")
    width += 2
    print()

height = int(input('Введите высоту бабочки: '))
x = 1
maxWidth = math.floor(height / 2) * 2
y = maxWidth - 2
for i in range(height):
    if i < math.floor(height / 2):
        for j in range(x):
            print("*", end="")
        for j in range(y):
            print(" ", end="")
        y -= 2
        for j in range(x):
            print("*", end="")
        x += 1
        print()
    elif i == math.floor(height / 2):
        x -= 1
        y += 2
    else:
        x -= 1
        for j in range(x):
            print("*", end="")
        y += 2
        for j in range(y):
            print(" ", end="")
        for j in range(x):
            print("*", end="")
        print()
print('Шахматная доска')
board = []
for _ in range(8):
    row = [' '] * 8
    board.append(row)
pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

for i in range(0, 8):
    for j in range(0, 8):
        if i % 2 == 1:
            if j % 2 == 1:
                board[i][j] = 'b'
            else:
                board[i][j] = 'w'
        else:
            if j % 2 == 1:
                board[i][j] = 'w'
            else:
                board[i][j] = 'b'

for i in range(8):
    board[0][i] += pieces[i]
    board[1][i] += 'p'
    board[6][i] += 'p'
    board[7][i] += pieces[i]

for i in range(8):
    for j in range(8):
        print(board[i][j] + " ", end='')
    print()

list = [10, 2, 40, 6, 60]
for i in range(len(list)):
    for j in range(0, len(list) - i - 1):
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
print(list)