from sqlalchemy import create_engine
from sqlalchemy.sql import text

def test_add_teacher():
    email = "marina56@yaa.com"

    conn = db.connect()
#добавляю учителя
insert_sql = text("INSERT INTO teacher (email) VALUES (:email)")
    conn.execute(insert_sql, {"email": email})
    conn.commit()

#ищу по email
select_sql = text("SELECT teacher_id, email FROM teacher WHERE email = :email")
    row = conn.execute(select_sql, {"email": email}).fetchone()

    assert row is not None, "Учитель не добавился — строка не найдена"
    teacher_id = row[0]
    assert row[1] == email

#удаляем учителя
delete_sql = text("DELETE FROM teacher WHERE teacher_id = :id")
    conn.execute(delete_sql, {"id": 34992})
    conn.commit()

    conn.close()
