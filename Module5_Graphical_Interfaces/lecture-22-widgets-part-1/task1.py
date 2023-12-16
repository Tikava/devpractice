import tkinter as tk
from tkinter import ttk

count = 0

def increment_count():
    global count
    count += 1
    count_label.config(text=f'Current count: {count}')
    
def double_count():
    global count
    count *= 2
    double_count_label.config(text=f'Doubled count: {count}')
    double_count_label.pack()
    
def reset_count():
    global count
    count = 0
    count_label.config(text=f'Current count: {count}')

root = tk.Tk()
root.title("My app")
root.geometry('400x200')

mainframe = ttk.Frame(root, padding=10)
mainframe.pack()

count_label = ttk.Label(mainframe, text=f'Current count: {count}')
count_label.pack()

double_count_label = ttk.Label(mainframe, text=f'Doubled count: {count}')
double_count_label.pack_forget()

ttk.Button(mainframe, text='Count', command=increment_count).pack()
ttk.Button(mainframe, text='Double', command=double_count).pack()
ttk.Button(mainframe, text='Reset', command=reset_count).pack()


root.mainloop()
