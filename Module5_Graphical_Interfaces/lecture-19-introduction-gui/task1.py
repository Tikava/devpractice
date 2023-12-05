from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
btn = ttk.Button(frm, text='Закрыть окно', command=root.destroy).grid(column=0, row=0)
root.mainloop()
