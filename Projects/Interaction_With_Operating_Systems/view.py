import tkinter as tk

class NoteView:
    def __init__(self, master):
        self.master = master
        self.master.title('Notes')

        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack()

        self.notes_listbox = tk.Listbox(self.main_frame, width=50, height=20)
        self.notes_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.notes_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.notes_listbox.config(yscrollcommand=self.scrollbar.set)
        
    def display_notes(self, notes):
        self.notes_listbox.delete(0, tk.END)
        for note in notes:
            self.notes_listbox.insert(tk.END, note.note_text)
