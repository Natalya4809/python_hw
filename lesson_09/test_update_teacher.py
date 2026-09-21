from sqlalchemy import create_engine
from sqlalchemy.sql import text

def test_update_teacher():
    email = "vika1234@gmail.ru"

#добавляю учителя
insert_sql = text("INSERT INTO teacher (email) VALUES (:email)")
    conn.execute(insert_sql, {"email": email})
    conn.commit()

#вношу изменения
sql = text("UPDATE teacher_id SET description = :descr WHERE email = :email")
    conn.execute(sql, {"descr": 'New descr', "email": email})

    transaction.commit()
    conn.close()

#удаляю учителя
delete_sql = text("DELETE FROM teacher WHERE teacher_id = :id")
    conn.execute(delete_sql, {"id": 34993})
    conn.commit()

    conn.close()



