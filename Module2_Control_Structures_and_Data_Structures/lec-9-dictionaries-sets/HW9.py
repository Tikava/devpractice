students = {'Arman': {'Phone': '87471234553', 'Address': 'Almaty city', 'email': 'arman2000@gmail.com'},
            'Bekbol': {'Phone': '87021230932', 'Address': 'Astana city', 'email': 'nagibatorBekbol@gmail.com'},
            'Askhat': {'Phone': '87041239412', 'Address': 'Karagandy city', 'email': '20052005askh@mail.ru'}}
print(students)
del students['Arman']
print(students)

A = {1, 2, 3, 4, 5, 6}
B = {3, 5, 6, 7, 4, 9}
print(A.intersection(B))
print(A.union(B))

countries = {}
# while True:
#     country = input('Введите название страны: ')
#     city = input('Введите название городе в этой стране: ')
#     if not country in countries:
#         countries[country] = [city]
#     else:
#         countries[country].append(city)
#     print("Успешно!")
#     print(countries)

inventory = {
    'items': [
        {'id': 0, 'name': 'Shoes', 'count': 200, 'price': 200},
        {'id': 1, 'name': 'Pants', 'count': 140, 'price': 50},
        {'id': 2, 'name': 'T-shirt', 'count': 100, 'price': 20},
        {'id': 3, 'name': 'Hat', 'count': 1000, 'price': 15},
        {'id': 4, 'name': 'Backpack', 'count': 2000, 'price': 30}
    ]
}

def showItem(id):
    return inventory['items'][id]

print(showItem(1))

def calculateAmount(inventory):
    sum = 0
    for item in inventory['items']:
        sum += item['price']
    return sum

print(calculateAmount(inventory))

def getIntersection(A, B):
    return A.intersection(B)

def getUnion(A, B):
    return A.union(B)
