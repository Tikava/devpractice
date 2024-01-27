import tkinter as tk
from functools import partial

def onclick(index):
    text = label.cget('text')
    if text == 'Nothing is selected':
        text = ''

    option_text = [f"Option {i + 1} is selected" for i, var in enumerate(variables) if var.get() == 1]
    text = '\n'.join(option_text)

    label.config(text=text)
        

root = tk.Tk()
root.geometry('800x400')
root.title('App')

options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
variables = []

for _ in range(len(options)):
    variables.append(tk.IntVar())

for i, option in enumerate(options):
    chckbttn = tk.Checkbutton(root, text=option, variable=variables[i], command=partial(onclick, i), onvalue=1, offvalue=0)
    chckbttn.pack()
    
label = tk.Label(root, text='Nothing is selected')
label.pack()

root.mainloop()