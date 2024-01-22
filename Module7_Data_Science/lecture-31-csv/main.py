import csv

file_path = 'data.csv'

with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if len(row['name']) < 6:
            print(row['name'])