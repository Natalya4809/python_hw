from sqlalchemy import create_engine
from sqlalchemy.sql import text

def test_delete_teacher():
    email = "larisa567@gmail.ru"

    conn = db.connect()

#добавляю учителя
insert_sql = text("INSERT INTO teacher (email) VALUES (:email)")
    conn.execute(insert_sql, {"email": email})
    conn.commit()

#удаляем учителя
delete_sql = text("DELETE FROM teacher WHERE teacher_id = :id")
    conn.execute(delete_sql, {"id": 34994})
    conn.commit()

    conn.close()







