import numpy

dictionary = {
    'movie': ['Gladiator', 'The matrix', 'The Godfather'],
    'song': ['ASAP - NewJeans', 'Cupid - FIFTY FIFTY', 'Lonely - Akon', 'Strangers - Kenya Grace']
}

def addMovie(name):
    dictionary['movie'].append(name)

def addSong(name):
    dictionary['song'].append(name)

# while True:
#     type = input('movie/song: ')
#     name = input('Enter name: ')
#     match type:
#         case 'movie':
#             addMovie(name)
#         case 'song':
#             addSong(name)
#         case default:
#             break
#     print('Успешно!')
#     print(dictionary)

students = {
    'Alisher': [4, 3, 5, 5, 3, 2, 2, 4, 4, 4, 4, 3, 3, 2, 4, 5],
    'Darmen': [3, 3, 3, 3, 3, 3, 4, 5, 2, 2, 2, 2, 2, 5, 5, 5],
    'Almat': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 4, 5, 5]
}

for student in students:
    print('Средняя оценка у ', student, ' - ' , numpy.average(students[student]))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def sum(matrix):
    sum = 0
    for row in matrix:
        for elem in row:
            sum += elem
    return sum

books = {
    'Novel Algorithms and Techniques in Telecommunications, Automation and Industrial Electronics': {
        'authors': 'Ausif Mahmood, Khaled Elleithy, Mohammad A. Karim, Tarek Sobh', 
        'isbn': '9781402087370', 
        'published': 'August 15, 2008'
    },
    'Pro Spring 5. An In-Depth Guide to the Spring Framework and Its Tools': {
        'authors': 'Iuliana Cosmina, Rob Harrop, Chris Schaefer, Clarence Ho', 
        'isbn': '9781484228081', 
        'published': 'October 11, 2017'
    },
}

def searchByAuthor(author):
    for book in books:
        if author in books[book]['authors']:
            print(book)

searchByAuthor('Ausif Mahmood')


x, y, z = 1, 2, 3
coordinates = (x, y, z)

def getCoordinatesSum(coordinates):
    return sum(coordinates)