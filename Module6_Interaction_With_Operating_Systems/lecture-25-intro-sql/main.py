from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
engine = create_engine('sqlite:///mydatabase.db')

Base.metadata.create_all(engine)

Session = sessionmaker(engine)

with Session() as session:
    person1 = Person(name='Toilybay', age=18)
    person2 = Person(name='Almat', age=18)
    session.add_all([person1, person2])
    session.commit()