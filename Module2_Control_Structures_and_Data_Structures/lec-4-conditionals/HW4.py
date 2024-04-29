a = int(input())
b = int(input())
if a > b:
    print('First number is greatest: ', a)
elif a < b:
    print('Second number is greatest: ', b)
else:
    print('Numbers are same')

c = int(input())
if c >= 10 and c <= 20:
    print('Число лежит в заданном диапазоне')
else:
    print('Число не лежит в заданном диапазоне')


age = int(input())
if age >= 18:
    print('You can drive a car')
else:
    print('You have to be at least 18 to drive a car')


grade = int(input())
if grade == 5:
    print('Отлично')
elif grade == 4:
    print('Хорошо')
elif grade == 3:
    print('Удовлетворительно')
elif grade == 1 or grade == 2:
    print('Не удовлетворительно')
else:
    print('Такой оценки нет')

personAge = int(input())
if personAge >= 0 and personAge < 2:
    print('Младенец')
elif personAge >= 2 and personAge < 12:
    print('Ребенок')
elif personAge >= 12 and personAge < 18:
    print('Подросток')
elif personAge >= 18 and personAge < 35:
    print('Молодежь')
elif personAge >= 35 and personAge < 60:
    print('Взрослый человек')
else:
    print('Пожилой человек')

number = int(input())
if number == 1:
    print('Первая четверть')
elif number == 2:
    print('Вторая четверть')
elif number == 3:
    print('Третья четверть')
else:
    print('Четвертая четверть')


n = int(input())
if n % 2 == 0:
    if n % 4 == 0:
        print('Число четное и делиться на 4')
    else:
        print('Число четное, но не делиться на 4')
else:
    print('Число не четное')

grade = int(input())
if grade == 10 or grade == 9:
    print('Отлично')
elif grade == 8 or grade == 7:
    print('Хорошо')
elif grade == 6 or grade == 5:
    print('Удовлетворительно')
else:
    print('Не удовлетворительно')
    hasAddictialTask = input('У ученика есть доп. работа? (Да/Нет): ')


num = int(input())
if num > 0 and num % 2 == 0:
    print('Число положительное и четное')

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Год високосный')
else:
    print('Год не високосный')

age = int(input())
healthy = input('True/False: ')
if (age >= 18 and age < 45) and healthy:
    print('Да может')
else:
    print('Не может')



print('Добро пожаловать на мини-квиз, у вас есть 7 вопросов')
correctAnswer = 0
ans1 = input('What is the capital of France?\nParis, London, Berlin, Madrid: ')
if ans1 == 'Paris':
    correctAnswer += 1
    print('Правильно\n')
else:
    print('Не правильно\n')
ans1 = input('What is the tallest mountain in the world?\nMount Everest, K2, Kangchenjunga, Lhotse: ')
if ans1 == 'Mount Everest':
    correctAnswer += 1
    print('Правильно\n')
else:
    print('Не правильно\n')
ans1 = input('Which is the largest ocean on Earth?\nPacific Ocean, Atlantic Ocean, Indian Ocean, Arctic Ocean: ')
if ans1 == 'Pacific Ocean':
    correctAnswer += 1
    print('Правильно\n')
else:
    print('Не правильно\n')
ans1 = input('In which year did the Titanic sink?\n1912, 1907, 1925, 1915: ')
if ans1 == '1912':
    correctAnswer += 1
    print('Правильно\n')
else:
    print('Не правильно\n')
ans1 = input('Who painted the Mona Lisa?\nLeonardo da Vinci, Michelangelo, Pablo Picasso, Vincent van Gogh: ')
if ans1 == 'Leonardo da Vinci':
    correctAnswer += 1
    print('Правильно\n')
else:
    print('What is the capital of Japan?\n')
ans1 = input('What is the capital of France?\nTokyo, Osaka, Kyoto, Seoul: ')
if ans1 == 'Tokyo':
    correctAnswer += 1
    print('Правильно\n')
else:
    print('Не правильно\n')
print('Вы ответили на ', correctAnswer, ' вопросов правильно')



username = 'tikava'
password = 'myPassword!!!'
inputUsername = input()
inputPassword = input()
if username == inputUsername and password == inputPassword:
    print('Вы зашли на сайт')
else:
    print('Данные введены не верно')


print('За доставку килограмма товара $4.55 и за расстояние 10 км $1.00')
weight = input('Вес товара в граммах: ')
distance = input('Расстояние до дома в км: ')
print('Доставк обойдется вам ', (weight / 1000) * 4.55 + distance / 10)