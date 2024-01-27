import tkinter as tk

task_list = []

def add_task():
    task_title = entry.get()
    if task_title:
        task_frame = tk.Frame(task_list_frame)
        task_frame.pack(anchor='w', padx=5, pady=2)  # Adjust padx and pady as needed
        
        task_label = tk.Label(task_frame, text=task_title, font=('TkDefaultFont', 12))
        task = {'title': task_label, 'done': tk.IntVar(value=0)}
        task_list.append(task)
        task_chkbtn = tk.Checkbutton(task_frame, command=handle_task, variable=task['done'], onvalue=1, offvalue=0)
        task_chkbtn.pack(side=tk.LEFT)
        task_label.pack(side=tk.LEFT)
    
def handle_task():
    for task in task_list:
        if task['done'].get() == 1:
            task['title'].config(font=('TkDefaultFont', 12, 'overstrike'))
        else:
            task['title'].config(font=('TkDefaultFont', 12, 'normal'))


root = tk.Tk()
root.title('To do list')
root.geometry('500x250')

label = tk.Label(root, text='Enter task...')
label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text='Submit', command=add_task)
submit_button.pack()

task_list_frame = tk.Frame(root)
task_list_frame.pack()

root.mainloop()