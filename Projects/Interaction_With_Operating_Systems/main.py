import tkinter as tk
from PIL import Image, ImageTk
from model import NoteModel
from view import NoteView
from controller import NoteController

class ImageButton(tk.Button):
    def __init__(self, master, image_path, command=None, width=None, height=None, **kwargs):
        img = Image.open(image_path)
        if width and height:
            img = img.resize((width, height))
        img = ImageTk.PhotoImage(img)
        super().__init__(master, image=img, command=command, borderwidth=0, **kwargs)
        self.image = img

class NoteApp:
    def __init__(self, master):
        self.master = master
        self.model = NoteModel()
        self.view = NoteView(master)
        self.controller = NoteController(self.model, self.view)
        
        self.view.notes_listbox.bind("<Double-Button-1>", self.edit_note)
        self.create_navigation_bar()
        
    def create_navigation_bar(self):
        self.nav_frame = tk.Frame(self.master)
        self.nav_frame.pack(side=tk.TOP, fill=tk.X)        

        self.settings_button = ImageButton(self.nav_frame, 'img/settings.png', width=20, height=20)
        self.settings_button.pack(side=tk.RIGHT, padx=5, pady=5)
        
        self.add_button = ImageButton(self.nav_frame, 'img/plus.png', command=self.add_note, width=20, height=20)
        self.add_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def add_note(self):
        new_note_window = tk.Toplevel(self.master)
        new_note_window.title("Add Note")
        
        note_label = tk.Label(new_note_window, text="Enter your note:")
        note_label.pack(padx=10, pady=10)
        
        note_entry = tk.Entry(new_note_window, width=50)
        note_entry.pack(padx=10, pady=5)
        
        save_button = tk.Button(new_note_window, text="Save", command=lambda: self.save_note(new_note_window, note_entry.get()))
        save_button.pack(pady=10)
        
    def edit_note(self, event):
        index = self.view.notes_listbox.curselection()
        if index:
            note_text = self.view.notes_listbox.get(index)
            edit_note_window = tk.Toplevel(self.master)
            edit_note_window.title("Edit Note")

            note_entry = tk.Entry(edit_note_window, width=50)
            note_entry.pack(padx=10, pady=5)
            note_entry.insert(tk.END, note_text)

            save_button = tk.Button(edit_note_window, text="Save", command=lambda: self.update_note(edit_note_window, index[0], note_entry.get()))
            save_button.pack(pady=10)
        else:
            tk.messagebox.showerror("Error", "Please select a note to edit.")

    def save_note(self, window, note_text):
        self.controller.add_note(note_text)
        window.destroy()
    
    def update_note(self, window, index, new_note_text):
        self.controller.update_note(index, new_note_text)
        window.destroy()

root = tk.Tk()
app = NoteApp(root)
root.mainloop()
