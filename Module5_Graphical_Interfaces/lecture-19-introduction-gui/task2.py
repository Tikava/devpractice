from tkinter import *
from tkinter import ttk

def updateLabel():
    label.config(text=f'Hello, {name_entry.get()}')

root = Tk()
root.title('My application')

mainframe = ttk.Frame(root, padding=10)
mainframe.grid()

name = StringVar()
name_entry = ttk.Entry(mainframe, textvariable=name)
name_entry.grid(column=0, row=1)

label = ttk.Label(mainframe, text='Hello')
label.grid(column=0, row=0)

btn = ttk.Button(mainframe, text='Say Hello',  command=updateLabel)
btn.grid(column=0, row=2)

root.mainloop()
