import datetime

class Calendar:
    
    def __init__(self):
        self.events = []
    
    def add_event(self, event):
        self.events.append(event)
        print('Ивент успешно добавлен в календарь')
        
    def remove_event(self, event):
        if event in self.events:
            self.events.remove(event)
            print('Ивент удален из календаря')
        else:
            print('Такого ивента нет в календаре')
    
    #Получаем ивенты по заданной дате
    def get_events_by_date(self, date):
        eventsOnDate = list()
        for event in self.events:
            if event['date'] == date:
                eventsOnDate.append(event)
                
        if len(eventsOnDate) > 0:
            print('Данные получены по заданной дате')
            return eventsOnDate
        
        print('Не получилось найти данные по заданной дате')
        return None
    
    def get_upcoming_events(self, forNDays):
        today = datetime.date.today()
        endDate = datetime.date(today.year, today.month, today.day + forNDays)
        
        resultedEvents = list()
        
        for event in self.events:
            if event['date'] <= endDate:
                resultedEvents.append(event)
        
        if len(resultedEvents) > 0:
            return resultedEvents
        
        print('Не удалось найти')
        return None   

    def __str__(self):
        return str(self.events)

# Конец класса

# Инитциализация        
event1 = {
    'name': 'Quiz #2 - DS and algorithms',
    'date': datetime.date(2023, 11, 18)
}

event2 = {
    'name': 'Quiz #2 - Statistics and Probability',
    'date': datetime.date(2023, 11, 18)
}

event3 = {
    'name': 'Midterm - Kazakh lang.',
    'date': datetime.date(2023, 11, 15)
}

event4 = {
    'name': 'New Year',
    'date': datetime.date(2024, 1, 1)
}

myCalendar = Calendar()
myCalendar.add_event(event1)
myCalendar.add_event(event2)
myCalendar.add_event(event3)
myCalendar.add_event(event4)

print(myCalendar)

print('Ивенты на сегодня:', myCalendar.get_events_by_date(datetime.date.today()))
print(myCalendar.get_upcoming_events(5))


#Заданиие - 2
class InventoryItem:

    def __init__(self, title, frequency, price):
        self.title = title
        self.frequency = frequency
        self.price = price
    
    def reduce_frequency(self, amount):
        if self.frequency >= amount:
            self.frequency -= amount
            print(f'Теперь количество товара с названием {self.title} - {self.frequency}')
        else:
            print(f'Не удалось уменьшить количество.\nКоличество этого товара в складе - {self.frequency}')
    
    def increase_frequency(self, amount):
        if amount > 0:
            self.frequency += amount
            print(f'Успешно изменили количество товаров.\nТеперь это - {self.frequency}')
        else:
            print('Не удалось совершить операцию. Число должно быть позитивным')
        
    def get_total_amount(self):
        return self.frequency * self.price
    
item1 = InventoryItem('Ball', 100, 10)
print('Общая сумма:', item1.get_total_amount())
item1.increase_frequency(1000)
item1.increase_frequency(-10)
item1.reduce_frequency(40)

#Задание - 3
class Student:
    
    def __init__(self, name, subjects = []):
        self.name = name
        self.subjects = subjects
    
    def add_subject(self, subject):
        self.subjects.append(subject)
        print('Предмет успешно добавлен')
    
    def put_grade(self, grade, subjectTitle):
        for subject in self.subjects:
            if subject['title'] == subjectTitle:
                subject['grade'] = grade
                print('Оценка поставлена')
                return
        # Кейс когда учитель поставил оценку по предмету которого нет у студента
        subject = {
            'title': subjectTitle,
            'grade': grade
        }
        self.add_subject(subject)
        print('Оценка поставлена')
        
    def get_GPA(self):
        if len(self.subjects) > 0:
            total_grade = 0
            for subject in self.subjects:
                total_grade += subject['grade']
            return total_grade / len(self.subjects)
        return None

student1 = Student('Toilybay', [
    {
        'title': 'Programming',
        'grade': 100
    },
    {
        'title': 'Math',
        'grade': 95
    }
])

print(student1.subjects)
print('Avg:', student1.get_GPA())
student1.put_grade(100, 'Math')
student1.put_grade(100, 'English')
print(student1.subjects)


class TicTacToe:
    def __init__(self):
        self.maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                          [0, 3, 6], [1, 4, 7], [2, 5, 8],
                          [0, 4, 8], [2, 4, 6]]
        self.game_over = False
        self.player1 = True

    def print_maps(self):
        for i in range(0, 9, 3):
            print(self.maps[i], self.maps[i+1], self.maps[i+2])

    def step_maps(self, step, symbol):
        if self.maps[step-1] not in ["X", "O"]:
            self.maps[step-1] = symbol
            return True
        else:
            return False

    def get_result(self):
        win = ""
        for i in self.victories:
            if self.maps[i[0]] == "X" and self.maps[i[1]] == "X" and self.maps[i[2]] == "X":
                win = "X"
            if self.maps[i[0]] == "O" and self.maps[i[1]] == "O" and self.maps[i[2]] == "O":
                win = "O"

        if win == "":
            if all(x in ["X", "O"] for x in self.maps):
                return "Draw"

        return win

    def play_game(self):
        while not self.game_over:
            self.print_maps()
            valid_move = False
            while not valid_move:
                if self.player1:
                    symbol = "X"
                    step_input = input("Человек 1, ваш ход: ")
                else:
                    symbol = "O"
                    step_input = input("Человек 2, ваш ход: ")

                if step_input.isdigit():
                    step = int(step_input)
                    if 1 <= step <= 9:
                        valid_move = self.step_maps(step, symbol)
                        if not valid_move:
                            print("Эта ячейка уже занята. Попробуйте другую.")
                    else:
                        print("Введите число от 1 до 9.")
                else:
                    print("Пожалуйста, введите цифру.")

            win = self.get_result()
            if win != "":
                self.game_over = True
            else:
                self.game_over = False

            self.player1 = not self.player1

        self.print_maps()
        if win == "Draw":
            print("Игра закончилась вничью")
        else:
            print("Победил", win)

# Для запуска игры:
game = TicTacToe()
game.play_game()
