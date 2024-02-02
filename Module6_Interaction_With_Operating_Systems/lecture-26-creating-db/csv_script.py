import sqlite3
import csv

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS new_people (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        gender TEXT
    );
    '''
)

with open('MOCK_DATA.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    cursor.executemany('INSERT INTO new_people VALUES(?, ?, ?, ?, ?);', csv_reader)

conn.commit()
conn.close()