for i in range(0, 21, 2):
    print(i)

print('Таблица умножения для числа n')
n = int(input('Введите число: '))
for i in range(11):
    print(i, '*', n, '=', i * n)

string = 'Python'
for letter in string:
    print(letter)

sum = 0
for i in range(1, 100, 2):
    sum += i
print('Сумма нечетных чисел до 100 - ', sum)


x = int(input('Введите число чтобы вывести на консоль все четные числа до введенного числа включительно: '))
for i in range(0, x + 1, 2):
    print(i)

y = int(input('Введите число для нахождения суммы: '))
sum = 0
for i in range(1, y):
    sum += i
print(sum)

#Пирамида
x = 1
for i in range(5):
    for j in range(x):
        print('*', end='') # Для вывода на одной строке
    x += 1
    print() # Для переноса на след. строку


print('Таблица для умножения')
for i in range(1, 6): # 1 - 5
    for j in range(0, 11):
        print(i, '*', j, '=', i * j)

number = int(input('Введите число чтобы проверить является ли число до него (включительно) простыми: '))
prime = True
for i in range(2, number + 1):
    for j in range(2, number + 1):
        if i != j and i % j == 0:
            prime = False
            break
    if prime:
        print('Число', i, 'простое')
    else:
        print('Число', i, 'не простое')
        prime = True

w = int(input('Введите число чтобы ввести все четные числа в диапазоне от 1 до заданного числа: '))
for i in range(2, w, 2):
    print(i)


#Мини-викторина
print('Добро пожаловать на мини викторину')
questions = [
    {
        'question': 'What is the capital of France?\nParis, London, Berlin, Madrid', 
        'answer': 'Paris'
    },
    {
        'question': 'What is the tallest mountain in the world?\nMount Everest, K2, Kangchenjunga, Lhotse', 
        'answer': 'Mount Everest'
    },
    {
        'question': 'Which is the largest ocean on Earth?\nPacific Ocean, Atlantic Ocean, Indian Ocean, Arctic Ocean', 
        'answer': 'Pacific Ocean'
    },
    {
        'question': 'In which year did the Titanic sink?\n1912, 1907, 1925, 1915', 
        'answer': '1912'
    },
    {
        'question': 'Who painted the Mona Lisa?\nLeonardo da Vinci, Michelangelo, Pablo Picasso, Vincent van Gogh', 
        'answer': 'Leonardo da Vinci'
    }
]

correctAnswerCount = 0
for question in questions:
    print(question['question'])
    inputAnswer = input()
    if inputAnswer == question['answer']:
        correctAnswerCount += 1
    print("Currect score: ", correctAnswerCount)
else:
    print('You have answered to ', correctAnswerCount, ' correct!')


print('''Угадаю твое загаданное число от 0 до 100 максимум за 7 шагов. 
Загадай число и отвечай мне тремья вариантами. 
Если твое число больше напиши Б, если меньше напиши М, иначе если я нашел твое число напиши Р.''')
tryCount = 0
r = 0
l = 100
mid = (r + l) // 2
print('Твое число больше/меньше/равно ', mid,  '? ')
answer = input()
while answer != 'Р':
    if answer == 'М':
        l = mid
        mid = (r + l) // 2
        print('Твое число больше/меньше/равно ', mid,  '? ')
        answer = input()
        tryCount += 1
    elif answer =='Б':
        r = mid
        mid = (r + l) // 2
        print('Твое число больше/меньше/равно ', mid,  '? ')
        answer = input()
        tryCount += 1
    else:
        print('Не правильно ввели, попробуйте заново')
        print('Твое число больше/меньше/равно ', mid,  '? ')
        answer = input()

print('Твое число ', mid, '.Я угадал твое число с ', tryCount + 1, 'попытки :)')