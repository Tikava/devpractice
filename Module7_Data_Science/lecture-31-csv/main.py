import csv

#Task 1
first_file_path = 'data.csv'

with open(first_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if len(row['name']) < 6:
            print(row['name'])

#Task 2
second_file_path = 'books.csv'

class BookManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None
    
    def set_reader(self):
        
        self.file = open(self.file_path, 'r')
        csv_reader = csv.DictReader(self.file)
        self.csv_reader = csv_reader                   
    
    def set_writer(self):
        fieldnames = ['id', 'title', 'author', 'publication_year']
        with open(self.file_path, 'a', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                csv_writer.writeheader()
            self.csv_writer = csv_writer
    
    def add_book(self, book):
        if not hasattr(self, 'csv_writer'):
            self.set_writer()
            
        with open(self.file_path, 'a', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=self.csv_writer.fieldnames)
            existing_ids = [int(row['id']) for row in self.get_reader()]
            max_id = max(existing_ids) + 1 if existing_ids else 1
            book['id'] = max_id
            csv_writer.writerow(book)
        print('Book has been added!')
    
    def get_reader(self):
        if not hasattr(self, 'csv_reader'):
            self.set_reader()
        return self.csv_reader
            
    
    def get_writer(self):
        return self.csv_writer
    
    def close_file(self):
        if self.file is not None and not self.file.closed:
            self.file.close()

bm = BookManager(second_file_path)
bm.set_writer()

def action1():    
    for row in bm.get_reader():
        print(f"Id: {row['id']}\nTitle: {row['title']}\nAuthor: {row['author']}\nPublication year: {row['publication_year']}")
        print('***')
        

def action2():
    book = {}
    book['title'] = input('Enter title: ')
    book['author'] = input('Enter author: ')
    book['publication_year'] = int(input('Enter publication year: '))
    bm.add_book(book)

while True:
    action = input('1.To list books.\n2.To add new book.\n3.To exit\n')
    match action:
        case '1':
            action1()
        case '2':
            action2()
        case '3':
            bm.close_file()
            break
        case default:
            print('Wrong action input. Please try again.')    