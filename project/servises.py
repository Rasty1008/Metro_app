from sqlmodel import SQLModel, create_engine


DATABASE_URL = 'postgresql://metro:password@localhost/metro_database'

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
'''
with engine.connect() as conn:
    result = conn.execute("Select 1")
    print(result)
'''