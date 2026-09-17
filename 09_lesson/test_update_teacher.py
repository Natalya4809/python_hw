from sqlalchemy import create_engine
from sqlalchemy.sql import text

def test_update():
    db = create_engine(db.connection_string)
    sql = text("UPDATE teacher SET description = :descr WHERE teacher_id = :teacher_id")
    rows = db.execute(sql, descr = 'New descr', teacher_id = 6555)