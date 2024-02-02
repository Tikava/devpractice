from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, insert

engine = create_engine('sqlite:///mydatabase.db')

metadata_obj = MetaData()

people_table = Table(
    'people', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

metadata_obj.create_all(engine)

with engine.connect() as conn:
    statement = insert(people_table).values(
        [
            {'name': 'devpractice', 'age': 10},
            {'name': 'qazdev', 'age': 15}
        ]
    )
    conn.execute(statement)
    conn.commit()

