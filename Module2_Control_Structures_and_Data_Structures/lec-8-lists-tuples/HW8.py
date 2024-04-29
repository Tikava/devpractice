import random


list = [1, 2, 3, 4, 5]
sum = 0
for item in list:
    sum += item
# print("Sum: ", sum)
# print("Avg: ", sum / len(list))

employeeInfo = ({'name': 'Employee 1', 'id': 0, 'phone': '87472564955'}, 
                {'name': 'Employee 2', 'id': 1, 'phone': '87472564933'}, 
                {'name': 'Employee 3', 'id': 2, 'phone': '87472564922'})
#print(employeeInfo[0])
haveToDelete = []
for i in range(len(list)):
    if list[i] % 2 == 1:
        haveToDelete.append(i)

haveToDelete.reverse()

for item in haveToDelete:
    del list[item]

fruits = ['Apple', 'Banana', 'Strawberry', 'Pineapple', 'Orange', 'Avocado']

for fruit in fruits:
    if len(fruit) < 5:
        fruits.pop(fruits.index(fruit))
#print(fruits)

students = [
    ('Alisher', 90),
    ('Almas', 65),
    ('Ivan', 100),
    ('Sergey', 85)
]

#print(students)

numbers = []
for i in range(21):
    if i % 2 == 0:
        numbers.append(i)

sum = 0
for number in numbers:
    sum += number * number
#print(sum)

matrix = [[random.randint(0, 99) for _ in range(10)] for _ in range(10)] #заполняем массив рандомными числами
sum = 0
for row in matrix:
    for number in row:
        sum += number
print(sum) #вывод суммы массива 10на10

