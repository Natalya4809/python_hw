from sqlalchemy import create_engine
from sqlalchemy.sql import text

def test_delete():
    db = create_engine(db.connection_string)
    sql = text("DELETE FROM company WHERE teacher_id = :teacher_id")
    rows = db.execute(sql, teacher_id = 6555)