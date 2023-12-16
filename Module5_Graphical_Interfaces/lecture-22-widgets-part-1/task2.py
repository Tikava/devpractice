import tkinter as tk
from tkinter import ttk

def make_regular():
    if text.tag_ranges('highlight'):
        start_index = text.index('highlight.first')
        end_index = text.index('highlight.last')
        text.tag_remove('bold', start_index, end_index)
        text.tag_remove('italic', start_index, end_index)
    else:
        text.tag_remove('bold', '1.0', tk.END)
        text.tag_remove('italic', '1.0', tk.END)

def make_bold():
    if text.tag_ranges('highlight'):
        start_index = text.index('highlight.first')
        end_index = text.index('highlight.last')
        text.tag_remove('italic', start_index, end_index) 
        text.tag_add('bold', start_index, end_index)
    else:
        text.tag_remove('italic', '1.0', tk.END)
        text.tag_add('bold', '1.0', tk.END)

def make_italic():
    if text.tag_ranges('highlight'):
        start_index = text.index('highlight.first')
        end_index = text.index('highlight.last')
        text.tag_remove('bold', start_index, end_index)
        text.tag_add('italic', start_index, end_index)
    else:
        text.tag_remove('bold', '1.0', tk.END)
        text.tag_add('italic', '1.0', tk.END)

root = tk.Tk()
root.title('My app')
root.geometry('400x200')

nav_bar = ttk.Frame(root, padding=10)
nav_bar.pack()

ttk.Button(nav_bar, text='Regular', command=make_regular).grid(row=0, column=0)
ttk.Button(nav_bar, text='Bold', command=make_bold).grid(row=0, column=1)
ttk.Button(nav_bar, text='Italic', command=make_italic).grid(row=0, column=2)

mainframe = ttk.Frame(root, padding=10)
mainframe.pack()

text = tk.Text(mainframe, height=10, width=40)
text.pack()

text.tag_configure('bold', font=('TkDefaultFont', 10, 'bold'))
text.tag_configure('italic', font=('TkDefaultFont', 10, 'italic'))
text.tag_configure('highlight', background='lightblue')

def highlight(event):
    text.tag_remove('highlight', '1.0', tk.END)
    if text.tag_ranges(tk.SEL):
        text.tag_add('highlight', tk.SEL_FIRST, tk.SEL_LAST)

text.bind('<<Selection>>', highlight)

root.mainloop()
