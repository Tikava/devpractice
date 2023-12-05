from tkinter import *
from tkinter import ttk

def on_pressed(*args):
    text.insert('1.0', user_entry.get())
    
def clear_text():
    text.delete('1.0', '2.0')

root = Tk()
root.title('Lecture 20 task2')

mainframe = ttk.Frame(root, padding=10)
mainframe.pack()

text = Text(mainframe)
text.insert('1.0', 'Sample Text')
text.pack()

ttk.Label(mainframe, text='Enter text').pack()

user_entry = ttk.Entry(mainframe)
user_entry.bind('<Return>', on_pressed)
user_entry.pack()

btn = ttk.Button(mainframe, text='Очистить все!', command=clear_text)
btn.pack()

root.mainloop()