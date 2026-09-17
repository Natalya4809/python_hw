from sqlalchemy import create_engine

db_connection_string = 'postgresql://postgres:12345@localhost:5432/Урок1'

db = create_engine(db_connection_string)

def test_db_connection():
    db = create_engine(db.connection_string)
    names = db.table_names()
    assert names [0] == 'group_student'


