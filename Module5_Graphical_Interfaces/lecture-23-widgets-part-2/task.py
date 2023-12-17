import tkinter as tk
from tkinter import ttk

# def on_mouse_move(event):
#     x = event.x 
#     y = event.y
#     canvas.create_oval(x, y, x + 1, y + 1, fill="black")

# root = tk.Tk()
# root.title('My app')
# root.geometry('400x200')


# selected_value = tk.StringVar()
# ttk.Combobox(mainframe, textvariable=selected_value, values=['1', '2', '3']).pack()


# scrollbar = tk.Scrollbar(mainframe)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# listbox = tk.Listbox(mainframe)
# listbox.pack()

# scrollbar.config(command=listbox.yview)

# for i in range(1, 21):
#     listbox.insert(tk.END, i) 
# menu = tk.Menu(root)
# root.config(menu=menu)

# submenu=tk.Menu(menu)
# menu.add_cascade(label='File', menu=submenu)
# submenu.add_command(label='Open', command=None)
# submenu.add_command(label='Quit', command=root.quit)

# edit_menu= tk.Menu(menu)
# menu.add_cascade(label='Edit', menu=edit_menu)
# edit_menu.add_command(label='Cancel')


root = tk.Tk()

list_items = ["Элемент 1", "Элемент 2", "Элемент 3"]

combo_box = ttk.Combobox(root, values=list_items)

combo_box.pack()

selected_items = []

def on_select(event):
    selected_item = combo_box.get()

    selected_items.append(selected_item)

    listbox.delete(0, tk.END)
    listbox.insert(tk.END, *selected_items)

combo_box.bind("<<ComboboxSelected>>", on_select)

listbox = tk.Listbox(root)

listbox.pack()

root.mainloop()





# canvas = tk.Canvas(mainframe, bg='white')
# canvas.pack()

# canvas.bind('<B1-Motion>', on_mouse_move)

# root.mainloop()