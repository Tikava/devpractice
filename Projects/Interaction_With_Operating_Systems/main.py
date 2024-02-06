import tkinter as tk 
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Notes')
root.geometry('400x600')

def create_image_button(image_path, command, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height)) 
    img = ImageTk.PhotoImage(img)
    button = tk.Button(nav_frame, image=img, command=command, borderwidth=0)
    button.image = img 
    return button

nav_frame = tk.Frame(root)
nav_frame.pack(side=tk.TOP, fill=tk.X)

add_button = create_image_button('img/plus.png', None, 24, 24)
add_button.pack(side=tk.LEFT, padx=5, pady=5)

settings_button = create_image_button('img/settings.png', None, 24, 24)
settings_button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()