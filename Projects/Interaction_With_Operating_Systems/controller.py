import tkinter as tk

class NoteController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.notes = self.model.get_notes()
        self.view.display_notes(self.notes)

    def add_note(self, note_text):
        self.model.add_note(note_text)
        self.notes = self.model.get_notes()
        self.view.display_notes(self.notes)

    def update_note(self, note_id, new_note_text):
        self.model.update_note(note_id, new_note_text)
        self.notes = self.model.get_notes()
        self.view.display_notes(self.notes)

    def delete_note(self, note_id):
        self.model.delete_note(note_id)
        self.notes = self.model.get_notes()
        self.view.display_notes(self.notes)