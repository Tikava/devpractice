import tkinter as tk
from tkinter import ttk

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result_label.config(text="Cannot divide by zero.")
                return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")

root = tk.Tk()
root.title("Enhanced Calculator")

mainframe = ttk.Frame(root, padding=10)
mainframe.grid()

entry_num1 = ttk.Entry(mainframe, width=10)
entry_num1.grid(column=0, row=0, padx=5, pady=5)

entry_num2 = ttk.Entry(mainframe, width=10)
entry_num2.grid(column=1, row=0, padx=5, pady=5)

ttk.Label(mainframe, text="Number 1:").grid(column=0, row=1)
ttk.Label(mainframe, text="Number 2:").grid(column=1, row=1)

calculate_button_add = ttk.Button(mainframe, text="Add", command=lambda: calculate("add"))
calculate_button_add.grid(column=0, row=2, pady=5)

calculate_button_subtract = ttk.Button(mainframe, text="Subtract", command=lambda: calculate("subtract"))
calculate_button_subtract.grid(column=1, row=2, pady=5)

calculate_button_multiply = ttk.Button(mainframe, text="Multiply", command=lambda: calculate("multiply"))
calculate_button_multiply.grid(column=0, row=3, pady=5)

calculate_button_divide = ttk.Button(mainframe, text="Divide", command=lambda: calculate("divide"))
calculate_button_divide.grid(column=1, row=3, pady=5)

result_label = ttk.Label(mainframe, text="Result:")
result_label.grid(column=0, row=4, columnspan=2, pady=10)

root.mainloop()
