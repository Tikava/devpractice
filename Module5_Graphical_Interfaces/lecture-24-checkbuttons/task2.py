import tkinter as tk
import data as DATA

data = DATA.data

def on_scroll(*args):
    text.yview(*args)
    
def on_filter_clicked():
    
    filtered_by_gender = [user for user in data if gender_chbtn_variables[user['sex']].get() == 1]
    filtered_by_age = [user for user in data if age_chbtn_variables[user['age']].get() == 1]
    filtered_by_city = [user for user in data if city_chbtn_variables[user['city']].get() == 1]

    merged_filtered_data = []
    for user in filtered_by_gender:
        if user not in merged_filtered_data:
            merged_filtered_data.append(user)
    
    for user in filtered_by_age:
        if user not in merged_filtered_data:
            merged_filtered_data.append(user)

    for user in filtered_by_city:
        if user not in merged_filtered_data:
            merged_filtered_data.append(user)
    
    my_string = text_formatter(merged_filtered_data)
    text.delete(1.0, "end")
    text.insert("end", my_string)

def text_formatter(data):
    full_text = ""
    for i, user in enumerate(data):
        info = f"User {i}:\nName:{user['name']}\nAge:{user['age']}\nCity:{user['city']}\nGender:{user['sex']}\n*****\n"
        full_text += info
        
    return full_text
    
root = tk.Tk()
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=1)
root.title('App')

frame_left = tk.Frame(root)
frame_right = tk.Frame(root)

frame_left.grid(row=0, column=0, sticky="nsew")
frame_right.grid(row=0, column=1, sticky="nsew")

text = tk.Text(root, wrap="word")
text.insert('end', text_formatter(data))
    
scrollbar = tk.Scrollbar(frame_left, command=on_scroll)

text.config(yscrollcommand=scrollbar.set)
text.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Checkboxes for gender
gender_options = ['male', 'female']
gender_chbtn_variables = {gender: tk.IntVar() for gender in gender_options}
for i, gender in enumerate(gender_options):
    chckbtn = tk.Checkbutton(frame_right, text=gender, variable=gender_chbtn_variables[gender], onvalue=1, offvalue=0, command=on_filter_clicked)
    chckbtn.grid(row=i+1, column=0, sticky="w")

gender_label = tk.Label(frame_right, text="Gender")
gender_label.grid(row=0, column=0, sticky="w")

# Checkboxes for age
min_age = min(user['age'] for user in data)
max_age = max(user['age'] for user in data)
age_chbtn_variables = {age: tk.IntVar() for age in range(min_age, max_age + 1)}
for i, age in enumerate(range(min_age, max_age + 1)):
    chckbtn = tk.Checkbutton(frame_right, text=str(age), variable=age_chbtn_variables[age], onvalue=1, offvalue=0, command=on_filter_clicked)
    chckbtn.grid(row=i+1, column=1, sticky="w")

age_label = tk.Label(frame_right, text="Age")
age_label.grid(row=0, column=1, sticky="w")

# Checkboxes for city
city_options = set(user['city'] for user in data)
city_chbtn_variables = {city: tk.IntVar() for city in city_options}
for i, city in enumerate(city_options):
    chckbtn = tk.Checkbutton(frame_right, text=city, variable=city_chbtn_variables[city], onvalue=1, offvalue=0, command=on_filter_clicked)
    chckbtn.grid(row=i+1, column=2, sticky="w")

city_label = tk.Label(frame_right, text="City")
city_label.grid(row=0, column=2, sticky="w")

root.mainloop()
