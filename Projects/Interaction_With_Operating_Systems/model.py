from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, Sequence('note_id_seq'), primary_key=True)
    note_text = Column(String)

class NoteModel:
    def __init__(self):
        self.engine = create_engine('sqlite:///notes.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_notes(self):
        session = self.Session()
        notes = session.query(Note).all()
        session.close()
        return notes

    def add_note(self, note_text):
        session = self.Session()
        new_note = Note(note_text=note_text)
        session.add(new_note)
        session.commit()
        session.close()

    def update_note(self, note_id, new_note_text):
        session = self.Session()
        note = session.query(Note).filter_by(id=note_id+1).first()
        if note:
            note.note_text = new_note_text
            session.commit()
        session.close()

    def delete_note(self, note_id):
        session = self.Session()
        note = session.query(Note).filter_by(id=note_id+1).first()
        if note:
            session.delete(note)
            session.commit()
        session.close()